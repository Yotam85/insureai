from __future__ import annotations

from typing import Any, List, Optional

from django.db import transaction
from django.utils.html import escape
from rest_framework import serializers

from .models import (
    Upload,
    EstimateJob,
    EstimateResult,
    Project,
    ContractorLead,
    ContractorLeadResponse,
)
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
    plan_ai_response = serializers.JSONField(read_only=True)
    plan_ai_payload = serializers.JSONField(read_only=True)
    plan_ai_updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model  = Project
        fields = [
            "id",
            "name",
            "zip",
            "created",
            "job_count",
            "plan_ai_payload",
            "plan_ai_response",
            "plan_ai_updated",
        ]



class AiPlanPayloadSerializer(serializers.Serializer):
    project = serializers.JSONField()
    slots = serializers.ListField(
        child=serializers.DictField(),
        required=False,
        allow_empty=True,
    )
    timeline = serializers.JSONField(required=False)
    unscheduledTaskIds = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )
    tasks = serializers.JSONField()

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        project = attrs.get("project") or {}
        if not isinstance(project, dict):
            raise serializers.ValidationError({"project": "must be an object"})

        raw_slots = attrs.get("slots")
        slots_input = raw_slots if isinstance(raw_slots, list) else []
        normalized_slots: list[dict[str, str]] = []
        for index, slot in enumerate(slots_input):
            if not isinstance(slot, dict):
                continue
            slot_id = str(slot.get("id") or "").strip()
            if not slot_id:
                slot_id = f"day-{index + 1}"
            slot_label = str(slot.get("label") or "").strip() or f"Day {index + 1}"
            if slot_id:
                normalized_slots.append({"id": slot_id, "label": slot_label})
        if not normalized_slots:
            normalized_slots = [{"id": f"day-{i + 1}", "label": f"Day {i + 1}"} for i in range(7)]
        attrs["slots"] = normalized_slots

        allowed_slot_ids = {slot["id"] for slot in normalized_slots}

        timeline_in = attrs.get("timeline") or {}
        if not isinstance(timeline_in, dict):
            timeline_in = {}

        tasks = attrs.get("tasks") or []
        if not isinstance(tasks, list):
            raise serializers.ValidationError({"tasks": "must be an array"})
        task_ids = {str(task.get("id")) for task in tasks if isinstance(task, dict) and "id" in task}

        normalized_timeline: dict[str, List[str]] = {}
        for raw_day, ids in timeline_in.items():
            day = str(raw_day)
            if allowed_slot_ids and day not in allowed_slot_ids:
                continue
            filtered: List[str] = []
            for value in ids or []:
                value_str = str(value)
                if value_str in task_ids:
                    filtered.append(value_str)
            normalized_timeline[day] = filtered
        attrs["timeline"] = normalized_timeline

        unscheduled = attrs.get("unscheduledTaskIds") or []
        attrs["unscheduledTaskIds"] = [str(tid) for tid in unscheduled if str(tid) in task_ids]
        return attrs


class AiPlanSaveSerializer(serializers.Serializer):
    payload = AiPlanPayloadSerializer()
    plan = serializers.JSONField()



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
            "claim_number", "claim_number_short", "property_type", "work_grade", "status", "created", "uploads"
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
    project = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    project_zip = serializers.SerializerMethodField()
    instructions = serializers.SerializerMethodField()
    peril   = serializers.SerializerMethodField()
    total_cost = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True, source="total_cost")
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "job_number", "job_title", "job_claim_short", "created",
            "project", "project_name", "project_zip",
            "inventory_status",
            "inventory_updated", "instructions", "peril", "total_cost", "pdf_url")

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

    def _project(self, obj):
        try:
            return getattr(obj.job, "project", None)
        except Exception:
            return None

    def get_project(self, obj):
        project = self._project(obj)
        return project.pk if project else None

    def get_project_name(self, obj):
        project = self._project(obj)
        return getattr(project, "name", "") if project else ""

    def get_project_zip(self, obj):
        project = self._project(obj)
        return getattr(project, "zip", "") if project else ""

    def get_instructions(self, obj):
        try:
            return obj.job.instructions
        except Exception:
            return ""


class ContractorLeadSerializer(serializers.ModelSerializer):
    job_id = serializers.IntegerField(source="job.pk", read_only=True)
    project_name = serializers.SerializerMethodField()
    project_zip = serializers.SerializerMethodField()
    job_instructions = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()
    responded = serializers.SerializerMethodField()
    responded_at = serializers.SerializerMethodField()

    class Meta:
        model = ContractorLead
        fields = [
            "id", "status", "headline", "summary", "total_cost",
            "line_items", "appendix", "metadata",
            "posted_at", "updated_at",
            "job_id", "project_name", "project_zip", "job_instructions",
            "pdf_url", "responded", "responded_at",
        ]
        read_only_fields = fields

    def get_project_name(self, obj):
        try:
            return getattr(obj.job.project, "name", "")
        except Exception:
            return ""

    def get_project_zip(self, obj):
        try:
            return getattr(obj.job.project, "zip", "")
        except Exception:
            return ""

    def get_job_instructions(self, obj):
        try:
            return obj.job.instructions
        except Exception:
            return ""

    def get_pdf_url(self, obj):
        result = getattr(obj, "result", None)
        file_field = getattr(result, "pdf_file", None)
        if not file_field:
            return None
        try:
            url = file_field.url
        except Exception:
            return None
        request = self.context.get("request")
        if request:
            try:
                return request.build_absolute_uri(url)
            except Exception:
                return url
        return url

    def _get_user_response(self, obj):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            return None
        try:
            return obj.responses.filter(contractor=user).first()
        except Exception:
            return None

    def get_responded(self, obj):
        return self._get_user_response(obj) is not None

    def get_responded_at(self, obj):
        resp = self._get_user_response(obj)
        if resp:
            return resp.created
        return None


class ContractorLeadResponseSerializer(serializers.ModelSerializer):
    contractor_name = serializers.SerializerMethodField()

    class Meta:
        model = ContractorLeadResponse
        fields = ["id", "lead", "contractor", "contractor_name", "decision", "note", "created", "updated"]
        read_only_fields = ["id", "lead", "contractor", "contractor_name", "created", "updated"]

    def get_contractor_name(self, obj):
        contractor = getattr(obj, "contractor", None)
        if not contractor:
            return ""
        return contractor.get_full_name() or contractor.username or contractor.email or f"User {contractor.pk}"


class ContractorLeadRespondSerializer(serializers.Serializer):
    note = serializers.CharField(max_length=600, required=False, allow_blank=True, allow_null=True)
    decision = serializers.ChoiceField(choices=ContractorLeadResponse.Decision.choices, required=False)

    def validate(self, attrs):
        if not attrs.get("note"):
            attrs["note"] = ""
        if not attrs.get("decision"):
            attrs["decision"] = ContractorLeadResponse.Decision.AVAILABLE
        return attrs

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
    project     = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    project_zip  = serializers.SerializerMethodField()
    inventory   = serializers.JSONField(required=False)
    has_inventory = serializers.SerializerMethodField()
    inventory_total = serializers.SerializerMethodField()
    inventory_html  = serializers.SerializerMethodField()
    created     = serializers.DateTimeField(read_only=True)
    inventory_status = serializers.CharField(read_only=True)
    inventory_updated = serializers.DateTimeField(read_only=True)
    total_cost  = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    pdf_url     = serializers.SerializerMethodField()
    uploads     = serializers.SerializerMethodField()
    html_report = serializers.SerializerMethodField()
    raw_json    = serializers.SerializerMethodField()
    instructions = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = (
            "id",
            "job",
            "job_number",
            "job_title",
            "job_claim_short",
            "created",
            "project",
            "project_name",
            "project_zip",
            "inventory_status",
            "inventory_updated",
            "inventory",
            "has_inventory",
            "inventory_total",
            "inventory_html",
            "raw_json",
            "total_cost",
            "pdf_url",
            "uploads",
            "html_report",
            "instructions",
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

    def _project(self, obj):
        try:
            return getattr(obj.job, "project", None)
        except Exception:
            return None

    def get_project(self, obj):
        project = self._project(obj)
        return project.pk if project else None

    def get_project_name(self, obj):
        project = self._project(obj)
        return getattr(project, "name", "") if project else ""

    def get_project_zip(self, obj):
        project = self._project(obj)
        return getattr(project, "zip", "") if project else ""

    def get_instructions(self, obj):
        try:
            return obj.job.instructions
        except Exception:
            return ""

    # ---- inventory helpers --------------------------------------
    def get_has_inventory(self, obj):
        try:
            inv = getattr(obj, "inventory", None) or []
            return bool(inv)
        except Exception:
            return False

    def _currency(self, obj) -> str:
        try:
            data = obj.raw_json or {}
            cur = (data.get("currency") or "USD") if isinstance(data, dict) else "USD"
            return str(cur)[:8]
        except Exception:
            return "USD"

    def _fmt_money(self, v, cur):
        try:
            return f"{cur} {float(v):,.2f}"
        except Exception:
            return f"{cur} {v}"

    def get_inventory_total(self, obj):
        try:
            inv = getattr(obj, "inventory", None) or []
            total = 0.0
            for row in inv:
                if not isinstance(row, dict):
                    continue
                q = float(row.get("quantity", 0) or 0)
                uc = float(row.get("unit_cost", 0) or 0)
                total += q * uc
            return total
        except Exception:
            return 0.0

    def get_inventory_html(self, obj):
        try:
            inv = getattr(obj, "inventory", None) or []
            if not inv:
                return ""
            cur = self._currency(obj)

            lines: list[str] = []
            lines.append('<div class="inventory-report">')
            lines.append('<h3>Materials Inventory</h3>')
            lines.append('<div style="overflow:auto">')
            lines.append('<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; min-width:560px">')
            lines.append('<thead><tr>'
                        '<th>Material</th>'
                        '<th>Qty</th>'
                        '<th>Unit</th>'
                        '<th>Unit Cost</th>'
                        '<th>Subtotal</th>'
                        '</tr></thead>')
            lines.append('<tbody>')
            total = 0.0
            for row in inv:
                if not isinstance(row, dict):
                    continue
                name = escape(str(row.get("name", "")))
                qty  = row.get("quantity", 0) or 0
                unit = escape(str(row.get("unit", "")))
                uc   = row.get("unit_cost", 0) or 0
                try:
                    qf = float(qty)
                    ucf = float(uc)
                except Exception:
                    qf = 0.0
                    ucf = 0.0
                sub = qf * ucf
                total += sub
                lines.append(
                    '<tr>'
                    f'<td>{name}</td>'
                    f'<td style="text-align:right">{qf:g}</td>'
                    f'<td>{unit}</td>'
                    f'<td style="text-align:right">{self._fmt_money(ucf, cur)}</td>'
                    f'<td style="text-align:right"><strong>{self._fmt_money(sub, cur)}</strong></td>'
                    '</tr>'
                )
            lines.append('</tbody>')
            lines.append(
                f'<tfoot><tr><td colspan="4" style="text-align:right"><strong>Total</strong></td>'
                f'<td style="text-align:right"><strong>{self._fmt_money(total, cur)}</strong></td></tr></tfoot>'
            )
            lines.append('</table>')
            lines.append('</div>')
            lines.append('</div>')
            return "\n".join(lines)
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
