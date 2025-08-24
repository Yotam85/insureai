# estimate/views.py
from __future__ import annotations

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView


from .models import Upload, EstimateJob, EstimateResult
from .serializers import (
    UploadSerializer,
    EstimateJobSerializer
)
from .tasks import run_estimate
from .utils import get_guest_key

# ---- config -------------------------------------------------

FREE_GUEST_JOB_LIMIT = 3   # or whatever you prefer

# ---- Uploads ------------------------------------------------

class UploadViewSet(viewsets.ModelViewSet):
    """
    POST /api/files/   (multipart/form-data) -> { id, file, mime }
    """
    serializer_class = UploadSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "guest_uploads"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Upload.objects.filter(owner=self.request.user)
        return Upload.objects.none()

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        gk   = get_guest_key(self.request)
        serializer.save(owner=user, guest_key=None if user else (gk or ""))


# ---- Jobs ---------------------------------------------------

class EstimateJobViewSet(viewsets.ModelViewSet):
    """
    POST /api/jobs/ with body:
    {
      "instructions": "...",
      "property_type": "res" | "com",
      "damage_type":   "water" | "fire" | "wind",
      "uploads": [<upload ids>]
    }
    """
    serializer_class = EstimateJobSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "guest_jobs"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return EstimateJob.objects.filter(owner=self.request.user)
        # guests can’t list all; they’ll hit /api/results/by-job/:id/
        return EstimateJob.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        gk   = get_guest_key(request)

        if not user and not gk:
            return Response({"detail": "Missing guest key."}, status=400)

        if not user:
            used = EstimateJob.objects.filter(guest_key=gk).count()
            if used >= FREE_GUEST_JOB_LIMIT:
                return Response(
                    {"detail": "Free trial limit reached.", "code": "guest_quota_exhausted"},
                    status=403,
                )

        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        job: EstimateJob = ser.save(owner=user, guest_key=None if user else (gk or ""))

        run_estimate.delay(job.id)
        return Response({"id": job.id}, status=status.HTTP_201_CREATED)


# ---- Results ------------------------------------------------
import logging
log = logging.getLogger(__name__)


# estimate/views.py
from .serializers import (
    EstimateResultListItemSerializer,
    EstimateResultDetailSerializer,  # <-- use this
)

class EstimateResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstimateResult.objects.all()
    serializer_class = EstimateResultDetailSerializer  # default, but we set explicitly in by_job too
    permission_classes = [AllowAny]

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

# ---- Optional utility endpoints ----------------------------

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
