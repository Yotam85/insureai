# insureai_core/views.py
from django.shortcuts import render

def landing(request):
    return render(request, "index.html")

# insureai_core/views.py
def landing(request):
    steps = [
        ("📤", "Upload Documents",
         "Upload property images, floor plans, and existing insurance policies. "
         "Our AI accepts multiple file formats."),
        ("🤖", "AI Analysis",
         "Our advanced AI analyzes your property details, identifies risks, "
         "and calculates coverage requirements."),
        ("📄", "Get Estimates",
         "Receive detailed insurance estimates with coverage recommendations "
         "and cost breakdowns."),
    ]
    return render(request, "index.html", {"steps": steps})


# accounts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from estimate.models import Upload, EstimateJob, EstimateResult
from estimate.utils import get_guest_key

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def claim_guest_work(request):
    gk = get_guest_key(request)
    if not gk:
        return Response({"detail": "guest_key missing."}, status=400)

    Upload.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)
    EstimateJob.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)
    EstimateResult.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)

    return Response({"detail": "Claimed."}, status=200)
