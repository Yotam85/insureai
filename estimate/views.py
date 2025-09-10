# estimate/views.py
from __future__ import annotations

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from django.db.models import Count


from .models import Upload, EstimateJob, EstimateResult, Project
from .serializers import (
    UploadSerializer,
    EstimateJobSerializer, ProjectSerializer
)

import json
from typing import Any, Dict, List, Union, Optional
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .tasks import run_estimate
from celery.result import AsyncResult
from .utils import get_guest_key
from .pdf_export import export_estimate_pdf_bytes


# estimate/views.py (add near imports)


FREE_GUEST_JOB_LIMIT = 1   # or whatever you prefer


# --- small helpers to normalize payloads safely ---
def _payload_for_pdf(payload: Union[Dict[str, Any], List[Any], str, bytes, None]) -> Dict[str, Any]:
    """
    Coerce whatever is stored in raw_json into the object shape our PDF wants:
    { items: [...], summary: { total_project_cost, estimate_reasoning, future_actions }, currency? }
    """
    # bytes/str -> parse
    if isinstance(payload, (bytes, bytearray)):
        try:
            payload = payload.decode("utf-8", errors="replace")
        except Exception:
            payload = ""
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            payload = {}

    # list -> wrap
    if isinstance(payload, list):
        total = 0.0
        for it in payload:
            try:
                total += float((it or {}).get("TOTAL_PRICE", 0) or 0)
            except Exception:
                pass
        return {
            "items": payload,
            "summary": {
                "total_project_cost": total,
                "estimate_reasoning": "",
                "future_actions": [],
            },
        }

    # dict -> ensure keys exist and are well-typed
    if isinstance(payload, dict):
        data: Dict[str, Any] = dict(payload)  # shallow copy
        # items
        items = data.get("items")
        if not isinstance(items, list):
            # support legacy sections[].items
            items = []
            for sec in (data.get("sections") or []) if isinstance(data.get("sections"), list) else []:
                its = (sec or {}).get("items")
                if isinstance(its, list):
                    items.extend([x for x in its if isinstance(x, dict)])
        data["items"] = items or []

        # summary
        summary = data.get("summary")
        if not isinstance(summary, dict):
            summary = {}
        # totals
        if "total_project_cost" not in summary:
            try:
                summary["total_project_cost"] = sum(float((i or {}).get("TOTAL_PRICE", 0) or 0) for i in data["items"])
            except Exception:
                summary["total_project_cost"] = 0.0
        summary.setdefault("estimate_reasoning", "")
        summary.setdefault("future_actions", [])
        data["summary"] = summary

        # sane default currency
        if not isinstance(data.get("currency"), str) or len(data.get("currency", "")) != 3:
            data["currency"] = "USD"

        return data

    # anything else
    return {
        "items": [],
        "summary": {"total_project_cost": 0.0, "estimate_reasoning": "", "future_actions": []},
        "currency": "USD",
    }

# estimate/views.py

import json
import logging
log = logging.getLogger(__name__)

FREE_GUEST_JOB_LIMIT = 3


# ---------- Projects ----------
class ProjectViewSet(viewsets.ModelViewSet):
    """
    /api/projects/
      GET -> list my projects (or guest projects)
      POST {name, zip} -> create or get existing for this identity
    /api/projects/:id/
      GET -> details
      DELETE -> remove (owner or guest only)
    """
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    throttle_classes: list = []

    @action(detail=True, methods=["get"])
    def jobs(self, request, pk=None):
        proj = self.get_object()  # ACL enforced by get_queryset
        qs = (EstimateJob.objects
              .filter(project=proj)
              .only("id", "claim_number", "project_seq", "title", "status", "agent_kind", "work_grade", "created")
              .order_by("-created"))
        data = [
            {
                "id": j.id,
                "number": j.project_seq,
                "title": j.title,
                "claim_number_short": (j.claim_number or "")[:15] if getattr(j, "claim_number", None) else "",
                "status": j.status,
                "work_grade": j.work_grade,
                "agent_kind": j.agent_kind,
                "created": j.created.isoformat() if j.created else None,
            }
            for j in qs
        ]
        return Response(data, status=200)
    
    def get_queryset(self):
        qs = Project.objects.all().annotate(job_count=Count("jobs")).order_by("-created", "-id")
        user = self.request.user if self.request.user.is_authenticated else None
        if user:
            return qs.filter(owner=user)
        gk = get_guest_key(self.request)
        if gk:
            return qs.filter(owner__isnull=True, guest_key=gk)
        return Project.objects.none()

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        gk   = get_guest_key(self.request)

        # idempotent "get or create" by identity+name+zip
        existing = None
        if user:
            existing = Project.objects.filter(owner=user, name=serializer.validated_data["name"], zip=serializer.validated_data["zip"]).first()
        elif gk:
            existing = Project.objects.filter(owner__isnull=True, guest_key=gk, name=serializer.validated_data["name"], zip=serializer.validated_data["zip"]).first()

        if existing:
            self.instance = existing
            return

        self.instance = serializer.save(owner=user, guest_key=None if user else (gk or ""))

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        self.perform_create(ser)
        # always return the (possibly existing) instance serialized with job_count
        inst = Project.objects.annotate(job_count=Count("jobs")).get(pk=self.instance.pk)
        out  = ProjectSerializer(inst).data
        return Response(out, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        proj = self.get_object()
        # ACL already enforced by get_queryset(); re-fetch with annotation
        proj = Project.objects.annotate(job_count=Count("jobs")).get(pk=proj.pk)
        return Response(ProjectSerializer(proj).data)

    def destroy(self, request, *args, **kwargs):
        proj = self.get_object()
        proj.delete()
        return Response(status=204)


# ---------- Uploads ----------
class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    permission_classes = [AllowAny]
    throttle_classes  = [ScopedRateThrottle]
    throttle_scope    = "guest_uploads"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Upload.objects.filter(owner=self.request.user)
        return Upload.objects.none()

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        gk   = get_guest_key(self.request)
        serializer.save(owner=user, guest_key=None if user else (gk or ""))


# estimate/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.db.models import Count
import logging

from .models import Upload, EstimateJob, Project
from .serializers import EstimateJobCreateSerializer, ProjectSerializer
from .tasks import run_estimate
from .utils import get_guest_key

log = logging.getLogger(__name__)

class EstimateJobViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    throttle_classes   = [ScopedRateThrottle]
    throttle_scope     = "guest_jobs"

    # Use the create serializer for POSTs; for GETs you can keep your detail serializer
    def get_serializer_class(self):
        if self.request.method == "POST":
            return EstimateJobCreateSerializer
        # fallback to whatever you use elsewhere (e.g., list/detail)
        from .serializers import EstimateJobSerializer
        return EstimateJobSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EstimateJob.objects.filter(owner=self.request.user).select_related("project")
        return EstimateJob.objects.none()

    def _get_project_checked(self, request, project_id: int) -> Project:
        proj = get_object_or_404(Project, pk=project_id)
        if request.user.is_authenticated:
            if proj.owner_id != request.user.id:
                # Hide existence
                raise get_object_or_404(Project, pk=0)
        else:
            gk = get_guest_key(request)
            if not gk or proj.owner_id is not None or proj.guest_key != gk:
                raise get_object_or_404(Project, pk=0)
        return proj

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=400)

        user = request.user if request.user.is_authenticated else None
        gk   = get_guest_key(request)

        project_id = ser.validated_data["project"].id if hasattr(ser.validated_data["project"], "id") else ser.validated_data["project"]
        try:
            proj = self._get_project_checked(request, project_id)
        except Exception as e:
            # Will be a 404; let it bubble
            raise

        # Optional uploads list
        upload_ids = ser.validated_data.pop("uploads", [])

        try:
            with transaction.atomic():
                job = EstimateJob.objects.create(
                    project=proj,
                    owner=user,
                    guest_key=None if user else (gk or ""),
                    title=ser.validated_data.get("title", ""),
                    agent_kind=ser.validated_data.get("agent_kind"),
                    instructions=ser.validated_data.get("instructions"),
                    property_type=ser.validated_data.get("property_type"),
                    work_grade=ser.validated_data.get("work_grade"),
                    status="PENDING",
                )

                # Attach uploads if provided (and belong to same identity)
                if upload_ids:
                    uq = Upload.objects.filter(pk__in=set(upload_ids))
                    if user:
                        uq = uq.filter(owner=user)
                    else:
                        uq = uq.filter(owner__isnull=True, guest_key=gk)
                    updated = uq.update(job=job)
                    if updated != len(set(upload_ids)):
                        log.warning("Some uploads not attached due to ACL mismatch or missing: requested=%s updated=%s",
                                    len(set(upload_ids)), updated)

            # Kick off Celery after commit
            transaction.on_commit(lambda: run_estimate.delay(job.id))
            return Response({"id": job.id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            log.exception("Job create failed: %s", e)
            # Bubble a helpful 400 instead of 500:
            return Response({"detail": f"Job creation failed: {type(e).__name__}: {e}"}, status=400)


# ---------- Results (unchanged except they continue to work) ----------
# ... (keep your existing EstimateResultViewSet, by_job, create_pdf, etc.)


# ---- Results ------------------------------------------------
import logging
log = logging.getLogger(__name__)


# estimate/views.py
from .serializers import (
    EstimateResultListItemSerializer,
    EstimateResultDetailSerializer,  # <-- use this
)

class EstimateResultViewSet(viewsets.ModelViewSet):
    queryset = EstimateResult.objects.all()
    serializer_class = EstimateResultDetailSerializer
    permission_classes = [AllowAny]
    throttle_classes: list = []

    @action(detail=False, methods=["get"], url_path="by-job/(?P<job_id>[^/.]+)")
    def by_job(self, request, job_id=None):
        gk = get_guest_key(request)
        try:
            job = EstimateJob.objects.get(pk=job_id)
        except EstimateJob.DoesNotExist:
            return Response({"detail": "Job not found."}, status=404)
        
        # ACL
        if request.user.is_authenticated:
            if job.owner_id != request.user.id:
                return Response({"detail": "Not found."}, status=404)
        else:
            if not gk or job.guest_key != gk:
                return Response({"detail": "Not found."}, status=404)

        try:
            result = job.estimateresult
        except EstimateResult.DoesNotExist:
            return Response({"status": job.status}, status=status.HTTP_202_ACCEPTED)

        # serialize with the safe detail serializer (includes html_report)
        data = EstimateResultDetailSerializer(result, context={"request": request}).data
        return Response(data, status=200)


    @action(detail=True, methods=["patch"])
    def update_json(self, request, pk=None):
        result = self.get_object()
        result.raw_json = request.data.get("raw_json", result.raw_json)
        result.save(update_fields=["raw_json"])
        return Response(self.get_serializer(result).data)
    
    
    @action(detail=True, methods=["post"])
    def create_pdf(self, request, pk=None):
        result = self.get_object()
        try:
            safe_payload = _payload_for_pdf(result.raw_json)

      

            pdf_bytes = export_estimate_pdf_bytes(safe_payload)

            # Replace previous PDF if present
            if result.pdf_file:
                try:
                    default_storage.delete(result.pdf_file.name)
                except Exception:
                    pass

            filename = f"estimates/job-{result.job_id}.pdf"
            saved = default_storage.save(filename, ContentFile(pdf_bytes))
            result.pdf_file = saved
            result.save(update_fields=["pdf_file"])
        except Exception as e:
            log.exception("create_pdf failed for result %s", pk)
            return Response({"detail": f"PDF generation failed: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = self.get_serializer(result, context={"request": request}).data
        return Response(data, status=200)

    @action(detail=True, methods=["get", "patch"], url_path="inventory")
    def inventory(self, request, pk=None):
        """Get or update the saved inventory for this result.
        Enforces the same ACL as by_job: owner or matching guest_key.
        GET returns { inventory: [...] }
        PATCH accepts { inventory: [...] } and saves it.
        """
        result = self.get_object()

        # ACL: allow only owner or matching guest
        job = getattr(result, "job", None)
        req = request
        if req.user.is_authenticated:
            if not job or job.owner_id != req.user.id:
                return Response({"detail": "Not found."}, status=404)
        else:
            gk = get_guest_key(req)
            if not gk or not job or job.owner_id is not None or job.guest_key != gk:
                return Response({"detail": "Not found."}, status=404)

        if request.method.lower() == "get":
            return Response({"inventory": result.inventory or []}, status=200)

        # PATCH
        inv = (request.data or {}).get("inventory", None)
        # Basic validation: must be a list of dict-like items
        if inv is None or not isinstance(inv, list):
            return Response({"detail": "inventory must be a list"}, status=400)
        # Normalize items
        cleaned = []
        for item in inv:
            if not isinstance(item, dict):
                continue
            cleaned.append({
                "name": str(item.get("name", ""))[:200],
                "quantity": float(item.get("quantity", 0) or 0),
                "unit": str(item.get("unit", "")).upper()[:16],
                "unit_cost": float(item.get("unit_cost", 0) or 0),
            })

        result.inventory = cleaned
        result.save(update_fields=["inventory"])
        return Response({"inventory": result.inventory}, status=200)

    @action(detail=True, methods=["post"], url_path="inventory/suggest")
    def inventory_suggest(self, request, pk=None):
        """
        Generate suggested inventory using the AI agent. Does not persist the suggestion.
        Accepts optional { items: [...] } in the body to override; otherwise uses result.raw_json.items.
        Returns { inventory: [...] } for the client to place into the form.
        """
        result = self.get_object()

        # ACL: same as inventory write
        job = getattr(result, "job", None)
        req = request
        if req.user.is_authenticated:
            if not job or job.owner_id != req.user.id:
                return Response({"detail": "Not found."}, status=404)
        else:
            gk = get_guest_key(req)
            if not gk or not job or job.owner_id is not None or job.guest_key != gk:
                return Response({"detail": "Not found."}, status=404)

        override = (request.data or {}).get("items")
        currency = (result.raw_json or {}).get("currency") if isinstance(result.raw_json, dict) else "USD"

        # Async path: queue a Celery task and return 202 with task id
        async_flag = str(request.query_params.get("async", "0")).strip() == "1"
        if async_flag:
            if isinstance(override, list):
                from .tasks import run_inventory_suggestion_with_override
                task = run_inventory_suggestion_with_override.delay(result.pk, override, currency or "USD")
            else:
                from .tasks import run_inventory_suggestion
                task = run_inventory_suggestion.delay(result.pk)
            return Response({"task": task.id}, status=status.HTTP_202_ACCEPTED)

        # Sync fallback: generate immediately
        from .tasks import generate_inventory_suggestion_from_items
        if isinstance(override, list):
            items = override
        else:
            data = result.raw_json or {}
            items = (data.get("items") or []) if isinstance(data, dict) else []
        inv = generate_inventory_suggestion_from_items(items, currency=currency or "USD")
        try:
            result.inventory = inv
            result.save(update_fields=["inventory"])
        except Exception:
            log.exception("Failed to save generated inventory for result %s", result.pk)
        return Response({"inventory": inv, "saved": True}, status=200)

    @action(detail=False, methods=["get", "post", "patch"], url_path="by-job/(?P<job_id>[^/.]+)/inventory/suggest")
    def inventory_suggest_by_job(self, request, job_id=None):
        """
        Convenience route to generate inventory suggestion by job id.
        - GET: use the job's EstimateResult.raw_json.items as input
        - POST/PATCH: if body includes { items: [...] }, use those instead
        Returns { inventory: [...] }. Never persists.
        """
        # Locate job and enforce ACL
        try:
            job = EstimateJob.objects.get(pk=job_id)
        except EstimateJob.DoesNotExist:
            return Response({"detail": "Job not found."}, status=404)

        if request.user.is_authenticated:
            if job.owner_id != request.user.id:
                return Response({"detail": "Not found."}, status=404)
        else:
            gk = get_guest_key(request)
            if not gk or job.guest_key != gk:
                return Response({"detail": "Not found."}, status=404)

        # Ensure result exists
        try:
            result = job.estimateresult
        except EstimateResult.DoesNotExist:
            return Response({"detail": "Result not ready."}, status=status.HTTP_202_ACCEPTED)

        override = (request.data or {}).get("items") if request.method.lower() in {"post", "patch"} else None
        currency = "USD"
        if isinstance(result.raw_json, dict):
            currency = result.raw_json.get("currency") or "USD"

        # Async path: queue a Celery task and return 202 with task id
        async_flag = str(request.query_params.get("async", "0")).strip() == "1"
        if async_flag:
            if isinstance(override, list):
                from .tasks import run_inventory_suggestion_with_override
                task = run_inventory_suggestion_with_override.delay(result.pk, override, currency)
            else:
                from .tasks import run_inventory_suggestion
                task = run_inventory_suggestion.delay(result.pk)
            return Response({"task": task.id}, status=status.HTTP_202_ACCEPTED)

        # Sync fallback
        from .tasks import generate_inventory_suggestion_from_items
        if isinstance(override, list):
            items = override
        else:
            data = result.raw_json or {}
            items = (data.get("items") or []) if isinstance(data, dict) else []
        inv = generate_inventory_suggestion_from_items(items, currency=currency)
        try:
            result.inventory = inv
            result.save(update_fields=["inventory"])
        except Exception:
            log.exception("Failed to save generated inventory for result %s", result.pk)
        return Response({"inventory": inv, "saved": True}, status=200)

    @action(detail=False, methods=["get"], url_path="inventory/suggest/status")
    def inventory_suggest_status(self, request):
        """Poll Celery task status: /api/results/inventory/suggest/status?task=<id>"""
        task_id = request.query_params.get("task")
        if not task_id:
            return Response({"detail": "Missing task id."}, status=400)
        res = AsyncResult(task_id)
        if res.successful():
            try:
                data = res.result or []
            except Exception:
                data = []
            return Response({"ready": True, "inventory": data}, status=200)
        if res.failed():
            return Response({"ready": False, "state": str(res.state), "detail": "failed"}, status=500)
        return Response({"ready": False, "state": str(res.state)}, status=202)
    

@api_view(["GET"])
@permission_classes([AllowAny])
def guest_quota(request):
    """GET /api/guest-quota/ → { remaining: <int|null> }"""
    if request.user.is_authenticated:
        return Response({"remaining": None})
    gk = get_guest_key(request)
    used = EstimateJob.objects.filter(guest_key=gk).count() if gk else 0
    return Response({"remaining": max(0, FREE_GUEST_JOB_LIMIT - used)})


# estimate/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import EstimateResult
from .utils import get_guest_key
import logging

def _row_for_result(r, request):
    # Use pk instead of id; and r.job_id is always available
    created_val = getattr(r, "created", None) or getattr(getattr(r, "job", None), "created", None)
    created = created_val.isoformat() if hasattr(created_val, "isoformat") else None

    try:
        pdf_url = request.build_absolute_uri(r.pdf_file.url) if getattr(r, "pdf_file", None) else None
    except Exception:
        pdf_url = None

    payload = r.raw_json or {}
    peril = payload.get("peril") or (payload.get("estimate") or {}).get("peril")

    return {
        "id": r.pk,          # 👈 pk works whether PK is job or id
        "job": r.job_id,
        "created": created,
        "premium": str(r.premium) if r.premium is not None else None,
        "peril": peril,
        "pdf_url": pdf_url,
    }

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def results_mine(request):
    try:
        qs = (EstimateResult.objects
              .filter(owner=request.user)
              .select_related("job")
              .order_by("-created")[:50])
        data = [_row_for_result(r, request) for r in qs]
        return Response(data, status=200)
    except Exception:
        logging.getLogger(__name__).exception("results_mine failed")
        return Response({"detail": "results_mine failed"}, status=500)

@api_view(["GET"])
@permission_classes([AllowAny])
def results_guest(request):
    try:
        gk = get_guest_key(request)
        if not gk:
            return Response([], status=200)
        qs = (EstimateResult.objects
              .filter(guest_key=gk, owner__isnull=True)
              .select_related("job")
              .order_by("-created")[:50])
        data = [_row_for_result(r, request) for r in qs]
        return Response(data, status=200)
    except Exception:
        logging.getLogger(__name__).exception("results_guest failed")
        return Response({"detail": "results_guest failed"}, status=500)
