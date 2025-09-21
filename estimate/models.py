# estimate/models.py
import uuid
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List

from django.conf import settings
from django.db import models


class Project(models.Model):
    """
    A user's place (e.g., a house) that groups estimate jobs together.
    For guests, we store guest_key until they sign in; then we migrate ownership.
    """
    name      = models.CharField(max_length=160)
    zip       = models.CharField(max_length=12)
    owner     = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="projects"
    )
    guest_key = models.CharField(max_length=64, blank=True, null=True, db_index=True)
    created   = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["owner", "created"]),
            models.Index(fields=["guest_key", "created"]),
        ]
        # Ensure deterministic pagination/listing order across admin and APIs
        ordering = ["-created", "-id"]

    def __str__(self) -> str:
        who = self.owner_id or (self.guest_key or "guest")
        return f"{self.name} ({self.zip}) • {who}"


class Upload(models.Model):
    file      = models.FileField(upload_to="%Y/%m/")
    guest_key = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    mime      = models.CharField(max_length=120)
    owner     = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  null=True, blank=True)
    job       = models.ForeignKey(
                  'EstimateJob',
                  on_delete=models.CASCADE,
                  null=True, blank=True,
                  related_name='uploads'
               )
    def __str__(self):
        return f"{self.file.name} ({self.mime})"


class EstimateJob(models.Model):
    guest_key = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    owner     = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    title       = models.CharField(max_length=160, blank=True, default="")
    project_seq = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    project   = models.ForeignKey(             # 👈 NEW
        Project,
        on_delete=models.CASCADE,
        null=True, blank=True,                 # keep nullable while backfilling; enforce in API
        related_name="jobs"
    )

    agent_kind = models.CharField(
        max_length=32,
        choices=[("insurance","insurance"), ("home_project","home_project"), ("contractor","contractor")],
        default="insurance",
    )

    instructions = models.TextField(
        blank=False,
        help_text="User’s description of the damage, context, etc."
    )

    claim_number = models.CharField(
        max_length=32,
        default=uuid.uuid4().hex,
        null=True, blank=True,
    )

    PROPERTY_CHOICES = [("res", "Residential"), ("com", "Commercial")]
    property_type = models.CharField(max_length=3, choices=PROPERTY_CHOICES,
                                     null=True, blank=True)

    # Deprecated: damage_type. Kept for backward compatibility; use work_grade instead.
    DAMAGE_CHOICES = [("water", "Water"), ("fire", "Fire"), ("wind", "Wind")]
    damage_type = models.CharField(max_length=5, choices=DAMAGE_CHOICES,
                                   null=True, blank=True)

    WORK_GRADE_CHOICES = [("low", "Low end"), ("standard", "Standard"), ("high", "High end")]
    work_grade = models.CharField(max_length=9, choices=WORK_GRADE_CHOICES,
                                  null=True, blank=True, help_text="Material/finish level")

    status  = models.CharField(max_length=12, default="PENDING")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        proj = f" • {self.project_id}" if self.project_id else ""
        t    = f" • {self.title}" if self.title else ""
        seq   = f" #{self.project_seq}" if self.project_seq else ""
        return f"Job{seq}{t} • {self.status}{proj}"

    def save(self, *args, **kwargs):
        # Assign per-project sequence on first save if missing
        if self.project_id and not self.project_seq:
            try:
                last = (
                    EstimateJob.objects
                    .filter(project_id=self.project_id)
                    .aggregate(models.Max("project_seq"))
                    .get("project_seq__max")
                ) or 0
                self.project_seq = last + 1
            except Exception:
                # Fallback if aggregation fails
                self.project_seq = self.project_seq or 1
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["project", "project_seq"], name="uniq_job_project_seq")
        ]


class EstimateResult(models.Model):
    job = models.OneToOneField(
        'EstimateJob',
        on_delete=models.CASCADE,
        related_name='estimateresult',
        primary_key=True,
    )
    owner     = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    guest_key = models.CharField(max_length=64, blank=True, null=True)
    raw_json  = models.JSONField(default=dict)
    inventory = models.JSONField(default=list, blank=True)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pdf_file  = models.FileField(upload_to="estimates/", null=True, blank=True)
    created   = models.DateTimeField(auto_now_add=True)


class ContractorLead(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        MATCHED = "matched", "Matched"
        CLOSED = "closed", "Closed"

    result = models.OneToOneField(
        'EstimateResult',
        on_delete=models.CASCADE,
        related_name='contractor_lead'
    )
    job = models.OneToOneField(
        'EstimateJob',
        on_delete=models.CASCADE,
        related_name='contractor_lead'
    )
    headline = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    line_items = models.JSONField(blank=True, default=list)
    appendix = models.JSONField(blank=True, default=dict)
    metadata = models.JSONField(blank=True, default=dict)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.OPEN)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-posted_at", "-id")

    def __str__(self) -> str:
        return f"Lead(job={self.job_id}, status={self.status})"

    @staticmethod
    def _to_decimal(value: Any) -> Decimal:
        if isinstance(value, Decimal):
            return value
        try:
            return Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError):
            return Decimal("0")

    @classmethod
    def build_payload_from_result(cls, result: 'EstimateResult') -> Dict[str, Any]:
        payload: Dict[str, Any] = {}
        raw: Dict[str, Any] = {}
        if isinstance(result.raw_json, dict):
            raw = result.raw_json

        items: List[Dict[str, Any]] = []
        total = Decimal("0")
        source_items: List[Dict[str, Any]] = []
        if isinstance(result.inventory, list):
            source_items = [v for v in result.inventory if isinstance(v, dict)]
        elif isinstance(raw.get("items"), list):
            source_items = [v for v in raw.get("items", []) if isinstance(v, dict)]

        for idx, item in enumerate(source_items, start=1):
            total_price = cls._to_decimal(item.get("TOTAL_PRICE") or item.get("total") or item.get("total_rcv"))
            total += total_price
            items.append({
                "id": item.get("id", idx),
                "description": item.get("line_items") or item.get("description") or item.get("item") or "",
                "category": item.get("category") or "General",
                "quantity": item.get("QUANTITY") or item.get("quantity") or item.get("qty") or 1,
                "unit": item.get("unit_code") or item.get("unit") or "EA",
                "unit_price": float(cls._to_decimal(item.get("UNIT_PRICE") or item.get("unit_price") or item.get("unit_rcv"))),
                "tax": float(cls._to_decimal(item.get("TAX") or item.get("tax"))),
                "total_price": float(total_price),
            })

        if not items and isinstance(raw.get("sections"), list):
            for section in raw.get("sections", []):
                items_in_section = section.get("items") if isinstance(section, dict) else []
                if not isinstance(items_in_section, list):
                    continue
                for idx, item in enumerate(items_in_section, start=len(items) + 1):
                    total_price = cls._to_decimal(item.get("TOTAL_PRICE") or item.get("total") or item.get("total_rcv"))
                    total += total_price
                    items.append({
                        "id": item.get("id", idx),
                        "description": item.get("line_items") or item.get("description") or item.get("item") or "",
                        "category": item.get("category") or (section.get("name") if isinstance(section, dict) else "General"),
                        "quantity": item.get("QUANTITY") or item.get("quantity") or item.get("qty") or 1,
                        "unit": item.get("unit_code") or item.get("unit") or "EA",
                        "unit_price": float(cls._to_decimal(item.get("UNIT_PRICE") or item.get("unit_price") or item.get("unit_rcv"))),
                        "tax": float(cls._to_decimal(item.get("TAX") or item.get("tax"))),
                        "total_price": float(total_price),
                    })

        if not total and isinstance(raw.get("summary"), dict):
            total = cls._to_decimal(raw.get("summary", {}).get("total_project_cost"))

        if not total and getattr(result, "total_cost", None):
            total = cls._to_decimal(result.total_cost)

        appendix = {}
        if isinstance(raw.get("appendix"), dict):
            appendix = raw.get("appendix")
        elif isinstance(raw.get("summary"), dict):
            appendix = {"summary": raw.get("summary")}

        payload.update({
            "items": items,
            "total_cost": total,
            "appendix": appendix,
            "metadata": {
                "currency": raw.get("currency", "USD"),
                "raw_summary": raw.get("summary"),
            },
        })
        return payload


class ContractorLeadResponse(models.Model):
    class Decision(models.TextChoices):
        AVAILABLE = "available", "Available"
        DECLINED = "declined", "Declined"

    lead = models.ForeignKey(ContractorLead, related_name="responses", on_delete=models.CASCADE)
    contractor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contractor_lead_responses", on_delete=models.CASCADE)
    decision = models.CharField(max_length=16, choices=Decision.choices, default=Decision.AVAILABLE)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("lead", "contractor")
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"LeadResponse(lead={self.lead_id}, contractor={self.contractor_id}, decision={self.decision})"
