# estimate/serializers.py
from rest_framework import serializers
from django.db import transaction

from .models import Upload, EstimateJob, EstimateResult
from .utils import get_guest_key  # <-- we’ll scope uploads by guest key

class UploadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model  = Upload
        fields = ["id", "file", "mime", "owner", "job"]   # owner/job read-only
        read_only_fields = ["owner", "job"]


# estimate/serializers.py
from rest_framework import serializers
from django.db import transaction
from .models import Upload, EstimateJob
from .utils import get_guest_key

class EstimateJobSerializer(serializers.ModelSerializer):
    property_type = serializers.ChoiceField(choices=[("res","res"),("com","com")])
    damage_type   = serializers.ChoiceField(choices=[("water","water"),("fire","fire"),("wind","wind")])

    # Keep queryset *broad* (only unattached); we’ll enforce ownership in validate_uploads
    uploads = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Upload.objects.filter(job__isnull=True),
        write_only=True,
        required=True,
    )

    class Meta:
        model  = EstimateJob
        fields = ["id","instructions","property_type","damage_type","uploads","status","created"]
        read_only_fields = ["status","created"]

    def validate_uploads(self, uploads):
        if not uploads:
            raise serializers.ValidationError("At least one upload is required.")

        request = self.context.get("request")
        user = getattr(request, "user", None)
        gk   = get_guest_key(request)

        errors = []
        for u in uploads:
            if user and user.is_authenticated:
                if u.owner_id != user.id:
                    errors.append(f"Upload {u.pk} does not belong to you.")
            else:
                if not gk:
                    errors.append("Missing guest key.")
                elif u.owner_id is not None or u.guest_key != gk:
                    errors.append(f"Upload {u.pk} does not belong to this guest.")
            if u.job_id is not None:
                errors.append(f"Upload {u.pk} is already attached to a job.")

        if errors:
            # Join all reasons so you see them in the Network tab
            raise serializers.ValidationError(errors)

        return uploads

    @transaction.atomic
    def create(self, validated_data):
        upload_list = validated_data.pop("uploads", [])
        job = EstimateJob.objects.create(**validated_data)
        Upload.objects.filter(pk__in=[u.pk for u in upload_list]).update(job=job)
        return job


# estimate/serializers.py
# estimate/serializers.py
# estimate/serializers.py
from rest_framework import serializers
from django.utils.html import escape
from .models import EstimateResult

class EstimateResultSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True) 
    job = serializers.IntegerField(source="job_id", read_only=True)
    created  = serializers.DateTimeField(read_only=True)   # 👈 add this
    pdf_url  = serializers.SerializerMethodField()
    uploads  = serializers.SerializerMethodField()
    html_report = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "created", "raw_json", "premium",
                  "pdf_url", "uploads", "html_report")



# --- Sidebar list item (lean) -----------------------------------------------
class EstimateResultListItemSerializer(serializers.ModelSerializer):
    job     = serializers.IntegerField(source="job_id", read_only=True)
    created = serializers.SerializerMethodField()
    peril   = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "created", "peril", "premium", "pdf_url")

    def get_created(self, obj):
        # tolerate older rows without .created
        try:
            return obj.created
        except Exception:
            try:
                return obj.job.created
            except Exception:
                return None

    def get_peril(self, obj):
        payload = obj.raw_json or {}
        # unified shape: payload["peril"]; legacy may nest
        return payload.get("peril") or (payload.get("estimate") or {}).get("peril")

    def _abs(self, url):
        if not url:
            return None
        req = self.context.get("request")
        return req.build_absolute_uri(url) if req else url

    def get_pdf_url(self, obj):
        f = getattr(obj, "pdf_file", None)
        if not f:
            return None
        try:
            return self._abs(f.url)
        except Exception:
            return None



# estimate/serializers.py
from rest_framework import serializers
from django.utils.html import escape
from .models import EstimateResult

class EstimateResultSafeSerializer(serializers.ModelSerializer):
    """Minimal, ultra-defensive serializer for by_job detail."""
    id       = serializers.IntegerField(source="pk", read_only=True)
    job      = serializers.IntegerField(source="job_id", read_only=True)
    created  = serializers.DateTimeField(read_only=True)
    pdf_url  = serializers.SerializerMethodField()
    uploads  = serializers.SerializerMethodField()
    raw_json = serializers.SerializerMethodField()  # avoid direct access surprises

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "created", "raw_json", "premium", "pdf_url", "uploads")

    def _abs(self, url):
        try:
            if not url:
                return None
            req = self.context.get("request")
            return req.build_absolute_uri(url) if req else url
        except Exception:
            return None

    def get_pdf_url(self, obj):
        try:
            f = getattr(obj, "pdf_file", None)
            return self._abs(f.url) if f else None
        except Exception:
            return None

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
            # if even that fails, return empty list rather than throw a 500
            return []
        return out

    def get_raw_json(self, obj):
        try:
            data = obj.raw_json or {}
            # ensure JSON-serializable fallback if any weird types sneak in
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}



# In your existing EstimateResultSerializer
def get_html_report(self, obj):
    try:
        payload = obj.raw_json or {}
        ...
        return "\n".join(lines)
    except Exception as e:
        # never let this break the API
        return "<div class='estimate-report'><p>Report not available.</p></div>"



# estimate/serializers.py
from rest_framework import serializers
from django.utils.html import escape
from .models import EstimateResult

class EstimateResultDetailSerializer(serializers.ModelSerializer):
    """
    Safe detail serializer used by /results/by-job/:id/
    Includes html_report, but never throws.
    """
    id       = serializers.IntegerField(source="pk", read_only=True)
    job      = serializers.IntegerField(source="job_id", read_only=True)
    created  = serializers.DateTimeField(read_only=True)
    pdf_url  = serializers.SerializerMethodField()
    uploads  = serializers.SerializerMethodField()
    html_report = serializers.SerializerMethodField()
    raw_json = serializers.SerializerMethodField()

    class Meta:
        model  = EstimateResult
        fields = ("id", "job", "created", "raw_json", "premium",
                  "pdf_url", "uploads", "html_report")

    # ---- helpers -------------------------------------------------
    def _abs(self, url):
        try:
            if not url:
                return None
            req = self.context.get("request")
            return req.build_absolute_uri(url) if req else url
        except Exception:
            return None

    # ---- fields --------------------------------------------------
    def get_pdf_url(self, obj):
        try:
            f = getattr(obj, "pdf_file", None)
            return self._abs(f.url) if f else None
        except Exception:
            return None

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
            data = obj.raw_json or {}
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    def get_html_report(self, obj):
        """
        Build a minimal HTML report; never throw.
        Fixes the 'lines is not defined' by defining it up front.
        """
        try:
            payload = obj.raw_json or {}
            summary = payload.get("summary") or {}
            items   = payload.get("items") or []

            # allow legacy shape: sections[].items
            if not items and isinstance(payload.get("sections"), list):
                items = []
                for s in payload["sections"]:
                    its = s.get("items") or []
                    if isinstance(its, list):
                        items.extend([it for it in its if isinstance(it, dict)])

            currency = payload.get("currency") or "USD"
            total    = summary.get("total_project_cost")
            reason   = summary.get("estimate_reasoning") or ""

            def fmt_money(v):
                try:
                    return f"{currency} {float(v):,.2f}"
                except Exception:
                    return f"{currency} {v}"

            # ✅ define lines up front so it's always in scope
            lines: list[str] = []
            lines.append('<div class="estimate-report">')
            lines.append('<h2>Estimate Summary</h2>')

            if total is not None:
                lines.append(f'<p><strong>Total Project Cost:</strong> {fmt_money(total)}</p>')

            if reason:
                lines.append('<h3>Reasoning</h3>')
                lines.append(f"<p>{escape(str(reason))}</p>")

            if items:
                lines.append('<h3>Line Items</h3>')
                lines.append('<table border="1" cellpadding="6" cellspacing="0">')
                lines.append('<thead><tr><th>#</th><th>Category</th><th>Description</th><th>Total</th></tr></thead>')
                lines.append("<tbody>")
                for idx, it in enumerate(items, 1):
                    cat   = it.get("category") or ""
                    desc  = it.get("line_items") or it.get("description") or ""
                    total_price = it.get("TOTAL_PRICE", "")
                    lines.append(
                        "<tr>"
                        f"<td>{idx}</td>"
                        f"<td>{escape(str(cat))}</td>"
                        f"<td>{escape(str(desc))}</td>"
                        f"<td style='text-align:right'>{fmt_money(total_price)}</td>"
                        "</tr>"
                    )
                lines.append("</tbody></table>")

            lines.append("</div>")
            return "\n".join(lines)
        except Exception:
            # Never break the endpoint
            return "<div class='estimate-report'><p>Report not available.</p></div>"
