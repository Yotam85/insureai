# estimate/models.py
import uuid
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
    # User-maintained inventory for this result (list of items)
    inventory = models.JSONField(default=list, blank=True)
    premium   = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    pdf_file  = models.FileField(upload_to="estimates/", null=True, blank=True)
    created   = models.DateTimeField(auto_now_add=True)
