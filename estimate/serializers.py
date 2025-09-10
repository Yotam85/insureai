from __future__ import annotations

from typing import Any, List, Optional

from django.db import transaction
from django.utils.html import escape
from rest_framework import serializers

from .models import Upload, EstimateJob, EstimateResult, Project
from .utils import get_guest_key


# -----------------------------
# Uploads
# -----------------------------
class UploadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model  = Upload
        fields = ["id", "file", "mime", "owner", "job"]
        read_only_fields = ["owner", "job"]



class ProjectSerializer(serializers.ModelSerializer):
    job_count = serializers.IntegerField(read_only=True)

    class Meta:
        model  = Project
        fields = ["id", "name", "zip", "created",
            "inventory_status",
            "inventory_updated", "job_count"]



class EstimateJobCreateSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=True)
    title   = serializers.CharField(max_length=160, required=False, allow_blank=True)
    work_grade = serializers.ChoiceField(choices=[("low","low"),("standard","standard"),("high","high")], required=False)
    uploads = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False,
        allow_empty=True
    )

    class Meta:
        model  = EstimateJob
        fields = ["project", "title", "agent_kind", "instructions", "property_type", "work_grade", "uploads"]

    def validate_instructions(self, v: str):
        if not v or len(v.strip()) < 5:
            raise serializers.ValidationError("Please describe the scope (≥ 5 chars).")
        return v.strip()

    def validate_agent_kind(self, v: str):
        allowed = {"insurance", "home_project", "contractor"}
        if v not in allowed:
            raise serializers.ValidationError(f"agent_kind must be one of {sorted(allowed)}")
        return v

    def validate_work_grade(self, v: str | None):
        if v is None or v == "":
            return None
        norm = str(v).strip().lower()
        mapping = {"low": "low", "low end": "low", "standard": "standard", "standert": "standard", "mid": "standard", "high": "high", "high end": "high"}
        if norm not in mapping:
            raise serializers.ValidationError("work_grade must be one of: low, standard, high")
        return mapping[norm]


# -----------------------------
# Jobs
# -----------------------------
class EstimateJobSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), required=True
    )
    title   = serializers.CharField(max_length=160, required=False, allow_blank=True)
    project_seq = serializers.IntegerField(read_only=True)
    claim_number_short = serializers.SerializerMethodField()
    property_type = serializers.ChoiceField(choices=[("res", "res"), ("com", "com")])
    work_grade    = serializers.ChoiceField(choices=[("low","low"),("standard","standard"),("high","high")], required=False)

    # Keep queryset broad (unattached only); enforce ownership in validate_uploads
    uploads = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Upload.objects.filter(job__isnull=True),
        write_only=True,
        required=True,
    )

    # Optional selector for triage override ("insurance" | "contractor" | "home_project")
    agent_kind = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model  = EstimateJob
        fields = [
            "id", "project", "title", "project_seq", "agent_kind", "instructions",
            "claim_number", "claim_number_short", "property_type", "work_grade", "status", "created"
        ]
        read_only_fields = ["status", "created"]

    def validate_uploads(self, uploads):
        if not uploads:
            raise serializers.ValidationError("At least one upload is required.")

        request = self.context.get("request")
        user = getattr(request, "user", None)
        gk   = get_guest_key(request)

        errors: List[str] = []
        for u in uploads:
            # owner/guest access control
            if user and user.is_authenticated:
                if u.owner_id != user.id:
                    errors.append(f"Upload {u.pk} does not belong to you.")
            else:
                if not gk:
                    errors.append("Missing guest key.")
                elif u.owner_id is not None or u.guest_key != gk:
                    errors.append(f"Upload {u.pk} does not belong to this guest.")
            # must be unattached
            if u.job_id is not None:
                errors.append(f"Upload {u.pk} is already attached to a job.")

        if errors:
            raise serializers.ValidationError(errors)

        return uploads

    @transaction.atomic
    def create(self, validated_data):
        upload_list = validated_data.pop("uploads", [])
        job = EstimateJob.objects.create(**validated_data)
        Upload.objects.filter(pk__in=[u.pk for u in upload_list]).update(job=job)
        return job

    def get_claim_number_short(self, obj):
        try:
            cn = getattr(obj, "claim_number", "") or ""
            return cn[:15]
        except Exception:
            return ""


# -----------------------------
# Results – list (lean for sidebar)
# -----------------------------
class EstimateResultListItemSerializer(serializers.ModelSerializer):
    id      = serializers.IntegerField(source="pk", read_only=True)
    job     = serializers.IntegerField(source="job_id", read_only=True)
    job_number = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    job_title = serializers.SerializerMethodField()
    job_claim_short = serializers.SerializerMethodField()
    peril   = serializers.SerializerMethodField()
    premium = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "job_number", "job_title", "job_claim_short", "created",
            "inventory_status",
            "inventory_updated", "peril", "premium", "pdf_url")

    def _abs(self, url: Optional[str]) -> Optional[str]:
        if not url:
            return None
        req = self.context.get("request")
        try:
            return req.build_absolute_uri(url) if req else url
        except Exception:
            return url

    def get_created(self, obj):
        # tolerate older rows without .created
        dt = getattr(obj, "created",
            "inventory_status",
            "inventory_updated", None) or getattr(getattr(obj, "job", None), "created",
            "inventory_status",
            "inventory_updated", None)
        return dt  # DRF will format DateTime

    def get_job_title(self, obj):
        try:
            return getattr(obj.job, "title", "")
        except Exception:
            return ""

    def get_job_number(self, obj):
        try:
            return getattr(obj.job, "project_seq", None)
        except Exception:
            return None

    def get_job_claim_short(self, obj):
        try:
            cn = getattr(obj.job, "claim_number", "") or ""
            return cn[:15]
        except Exception:
            return ""

    def get_peril(self, obj):
        payload = obj.raw_json or {}
        return payload.get("peril") or (payload.get("estimate") or {}).get("peril")

    def get_pdf_url(self, obj):
        f = getattr(obj, "pdf_file", None)
        if not f:
            return None
        try:
            return self._abs(f.url)
        except Exception:
            return None

import json
# serializers.py
from typing import Any, Dict, List, Optional
from django.utils.html import escape



# -----------------------------
# Results – detail (used by /results/by-job/:id/)
# -----------------------------
class EstimateResultDetailSerializer(serializers.ModelSerializer):
    id          = serializers.IntegerField(source="pk", read_only=True)
    job         = serializers.IntegerField(source="job_id", read_only=True)
    job_title   = serializers.SerializerMethodField()
    job_number  = serializers.SerializerMethodField()
    job_claim_short = serializers.SerializerMethodField()
    inventory   = serializers.JSONField(required=False)
    created     = serializers.DateTimeField(read_only=True)
    inventory_status = serializers.CharField(read_only=True)
    inventory_updated = serializers.DateTimeField(read_only=True)
    premium     = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    pdf_url     = serializers.SerializerMethodField()
    uploads     = serializers.SerializerMethodField()
    html_report = serializers.SerializerMethodField()
    raw_json    = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = (
            "id",
            "job",
            "job_number",
            "job_title",
            "job_claim_short",
            "created",
            "inventory_status",
            "inventory_updated",
            "inventory",
            "raw_json",
            "premium",
            "pdf_url",
            "uploads",
            "html_report",
        )

    # ---- helpers -------------------------------------------------
    def _abs(self, url: Optional[str]) -> Optional[str]:
        if not url:
            return None
        req = self.context.get("request")
        try:
            return req.build_absolute_uri(url) if req else url
        except Exception:
            return url

    # ---- fields --------------------------------------------------
    def get_pdf_url(self, obj):
        try:
            f = getattr(obj, "pdf_file", None)
            return self._abs(f.url) if f else None
        except Exception:
            return None

    def get_job_title(self, obj):
        try:
            return getattr(obj.job, "title", "")
        except Exception:
            return ""

    def get_job_number(self, obj):
        try:
            return getattr(obj.job, "project_seq", None)
        except Exception:
            return None

    def get_job_claim_short(self, obj):
        try:
            cn = getattr(obj.job, "claim_number", "") or ""
            return cn[:15]
        except Exception:
            return ""

    def get_uploads(self, obj):
        out = []
        try:
            for up in obj.job.uploads.all():
                try:
                    url = self._abs(getattr(up.file, "url", None))
                except Exception:
                    url = None
                out.append({"id": up.id, "file": url or "", "mime": up.mime})
        except Exception:
            return []
        return out

    def get_raw_json(self, obj):
        try:
            data = obj.raw_json
            # Pass through dicts and lists as-is (both are valid JSON roots)
            if isinstance(data, (dict, list)):
                return data
            # If something stored a string, try to decode it
            if isinstance(data, str):
                try:
                    parsed = json.loads(data)
                    return parsed if isinstance(parsed, (dict, list)) else {"_raw_text": data}
                except Exception:
                    return {"_raw_text": data}
            # Unknown type → make it serializable but don’t hide it
            return {"_repr": repr(data)}
        except Exception:
            return {}


    def get_html_report(self, obj):
        """
        Build an HTML report that works with:
        - dict payloads: { items: [...], summary: {...}, currency?: "USD" }
        - legacy dicts: { sections: [{items: [...]}], ... }
        - list root:    [ {...}, {...} ]   (treated as items)
        Never throws.
        """
        try:
            # --- normalize payload to { items: [...], summary: {...}, currency: ... } ---
            data = obj.raw_json
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except Exception:
                    data = {}

            currency = "USD"
            items: List[Dict[str, Any]] = []
            summary: Dict[str, Any] = {}

            if isinstance(data, list):
                # list root → treat as items
                items = [it for it in data if isinstance(it, dict)]
            elif isinstance(data, dict):
                currency = data.get("currency") or "USD"
                if isinstance(data.get("items"), list):
                    items = [it for it in data["items"] if isinstance(it, dict)]
                elif isinstance(data.get("sections"), list):  # legacy
                    for sec in data["sections"]:
                        for it in (sec or {}).get("items") or []:
                            if isinstance(it, dict):
                                items.append(it)
                summary = data.get("summary") or {}

            # fill summary total if missing
            if "total_project_cost" not in summary:
                total_sum = 0.0
                for it in items:
                    try:
                        total_sum += float(it.get("TOTAL_PRICE", 0) or 0)
                    except Exception:
                        pass
                summary["total_project_cost"] = total_sum

            reason = (summary.get("estimate_reasoning") or "").strip()

            def m(v):
                try:
                    return f"{currency} {float(v):,.2f}"
                except Exception:
                    return f"{currency} {v}"

            # --- render HTML ---
            lines: List[str] = []
            lines.append('<div class="estimate-report">')
            lines.append('<h2>Estimate Summary</h2>')
            lines.append(
                f"<p><strong>Total Project Cost:</strong> {m(summary.get('total_project_cost', 0))}</p>"
            )

            if reason:
                lines.append('<h3>Reasoning</h3>')
                lines.append(f"<p>{escape(reason)}</p>")

            if items:
                lines.append('<h3>Line Items</h3>')
                lines.append('<div style="overflow:auto">')
                lines.append(
                    '<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; min-width:720px">'
                )
                lines.append(
                    "<thead><tr>"
                    "<th>#</th><th>Item</th><th>Qty</th><th>Unit</th>"
                    "<th>Unit Price</th><th>Tax</th><th>Total</th><th>Category</th>"
                    "</tr></thead>"
                )
                lines.append("<tbody>")
                for idx, it in enumerate(items, 1):
                    desc = it.get("line_items") or it.get("description") or ""
                    qty  = it.get("QUANTITY", "")
                    unit = it.get("unit_code") or it.get("unit") or ""
                    up   = it.get("UNIT_PRICE", 0)
                    tax  = it.get("TAX", 0)
                    tot  = it.get("TOTAL_PRICE", 0)
                    cat  = it.get("category", "")
                    lines.append(
                        "<tr>"
                        f"<td>{idx}</td>"
                        f"<td>{escape(str(desc))}</td>"
                        f"<td style='text-align:right'>{escape(str(qty))}</td>"
                        f"<td>{escape(str(unit))}</td>"
                        f"<td style='text-align:right'>{m(up)}</td>"
                        f"<td style='text-align:right'>{m(tax)}</td>"
                        f"<td style='text-align:right'><strong>{m(tot)}</strong></td>"
                        f"<td>{escape(str(cat))}</td>"
                        "</tr>"
                    )
                lines.append("</tbody></table>")
                lines.append("</div>")  # overflow wrapper

                # Optional appendix with details/tags/source
                if any(it.get("Details") or it.get("tags") or it.get("source") for it in items):
                    lines.append('<h3 style="margin-top:1.25rem">Item Details</h3>')
                    for idx, it in enumerate(items, 1):
                        desc = it.get("line_items") or it.get("description") or ""
                        details = (it.get("Details") or "").strip()
                        tags = it.get("tags") or []
                        src  = it.get("source") or {}
                        if not (details or tags or src):
                            continue
                        lines.append(f"<p><strong>#{idx} — {escape(str(desc))}</strong></p>")
                        if details:
                            lines.append(f"<p>{escape(details)}</p>")
                        extra_bits = []
                        if tags:
                            try:
                                extra_bits.append("Tags: " + ", ".join(map(escape, map(str, tags))))
                            except Exception:
                                pass
                        if isinstance(src, dict) and (src.get("file") or src.get("page")):
                            parts = []
                            if src.get("file"): parts.append(f"file: {escape(str(src['file']))}")
                            if src.get("page"): parts.append(f"page: {escape(str(src['page']))}")
                            if parts:
                                extra_bits.append("Source: " + ", ".join(parts))
                        if extra_bits:
                            lines.append("<p>" + " &nbsp; | &nbsp; ".join(extra_bits) + "</p>")

            lines.append("</div>")
            return "\n".join(lines)
        except Exception:
            return "<div class='estimate-report'><p>Report not available.</p></div>"


# Backwards-compat alias (some code imports this name)
EstimateResultSerializer = EstimateResultDetailSerializer
