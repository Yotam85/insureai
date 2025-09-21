import hashlib, random, re
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action

from .models import LoginCode, ContractorProfile, User
from estimate.utils import get_guest_key
from estimate.models import Upload, EstimateJob, EstimateResult, Project

CODE_TTL_MIN = 10
MAX_ATTEMPTS = 5
EMAIL_RE     = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def _hash_code(email: str, code: str) -> str:
    s = f"{settings.SECRET_KEY}:{email.lower().strip()}:{code.strip()}"
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import logging
logger = logging.getLogger(__name__)

def _send_code_email(email: str, code: str) -> None:
    """Send a nicely formatted sign-in code email with HTML + plain text."""
    try:
        subject = "Your Estimai sign-in code"
        ctx = {"code": code, "ttl": CODE_TTL_MIN, "product": "Estimai"}
        # Render templates (falls back gracefully if templates missing)
        try:
            html_body = render_to_string("accounts/login_code_email.html", ctx)
        except Exception:
            html_body = None
        try:
            text_body = render_to_string("accounts/login_code_email.txt", ctx)
        except Exception:
            text_body = f"Your sign-in code is: {code}\nThis code expires in {CODE_TTL_MIN} minutes.\n"

        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            to=[email],
        )
        if html_body:
            msg.attach_alternative(html_body, "text/html")
        msg.send(fail_silently=False)
    except Exception:
        logger.exception("Failed to send sign-in code email")
        raise


class StartLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = (request.data.get("email") or "").strip().lower()
        if not EMAIL_RE.match(email):
            return Response({"detail": "Invalid email."}, status=400)

        code = f"{random.randint(0, 999999):06d}"

        LoginCode.objects.create(
            email=email,
            code_hash=_hash_code(email, code),
            guest_key=get_guest_key(request) or "",
            expires_at=timezone.now() + timedelta(minutes=CODE_TTL_MIN),
        )
        _send_code_email(email, code)
        return Response({"detail": "Code sent."}, status=200)

class VerifyCode(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = (request.data.get("email") or "").strip().lower()
        code  = (request.data.get("code") or "").strip()
        if not EMAIL_RE.match(email) or not re.fullmatch(r"\d{6}", code):
            return Response({"detail": "Invalid email or code."}, status=400)

        now = timezone.now()
        lc = (
            LoginCode.objects
            .filter(email=email, used_at__isnull=True, expires_at__gt=now)
            .order_by("-created_at")
            .first()
        )
        if not lc:
            return Response({"detail": "Code expired. Request a new one."}, status=400)
        if lc.attempts >= MAX_ATTEMPTS:
            return Response({"detail": "Too many attempts. Request a new code."}, status=429)
        if lc.code_hash != _hash_code(email, code):
            lc.attempts += 1
            lc.save(update_fields=["attempts"])
            return Response({"detail": "Incorrect code."}, status=400)

        lc.used_at = now
        lc.save(update_fields=["used_at"])

        User = get_user_model()
        user, _ = User.objects.get_or_create(email=email, defaults={"username": email})
        token, _ = Token.objects.get_or_create(user=user)

        # auto-claim guest work (uploads, jobs, results) by guest key
        gk = get_guest_key(request)
        if gk:
            # Transfer guest-owned entities to this user, including projects
            Project.objects.filter(guest_key=gk, owner__isnull=True).update(owner=user, guest_key=None)
            Upload.objects.filter(guest_key=gk, owner__isnull=True).update(owner=user, guest_key=None)
            EstimateJob.objects.filter(guest_key=gk, owner__isnull=True).update(owner=user, guest_key=None)
            EstimateResult.objects.filter(guest_key=gk, owner__isnull=True).update(owner=user, guest_key=None)

        return Response({"token": token.key, "user": {"id": user.id, "email": user.email}}, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({"detail": "Logged out."}, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def claim_guest_work(request):
    gk = get_guest_key(request)
    if not gk:
        return Response({"detail": "guest_key missing."}, status=400)

    # Transfer ownership of everything, including projects
    Project.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)
    Upload.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)
    EstimateJob.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)
    EstimateResult.objects.filter(guest_key=gk, owner__isnull=True).update(owner=request.user, guest_key=None)

    return Response({"detail": "Claimed."}, status=200)


# -------- Contractor role/profile endpoints --------
from rest_framework import viewsets
from .serializers import ContractorProfileSerializer, ContractorIdentitySerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class ContractorMeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="register")
    def register(self, request):
        user = request.user
        # Promote the authenticated user to contractor role when they explicitly register
        if getattr(user, "role", None) != User.Role.CONTRACTOR:
            user.role = User.Role.CONTRACTOR
            user.save(update_fields=["role"])
        prof, _ = ContractorProfile.objects.get_or_create(user=user)
        ser = ContractorProfileSerializer(prof, data=request.data, partial=True, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)

    @action(detail=False, methods=["get", "patch"], url_path="me")
    def me(self, request):
        if request.method == "GET":
            prof = ContractorProfile.objects.filter(user=request.user).first()
            if not prof:
                return Response({"detail": "Contractor profile not found."}, status=404)
            return Response(ContractorProfileSerializer(prof, context={"request": request}).data)
        prof = ContractorProfile.objects.filter(user=request.user).first()
        if not prof:
            prof = ContractorProfile.objects.create(user=request.user)
        ser = ContractorProfileSerializer(prof, data=request.data, partial=True, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    @action(detail=False, methods=["get"], url_path="status")
    def status(self, request):
        prof = ContractorProfile.objects.filter(user=request.user).first()
        role = getattr(request.user, "role", None)
        is_contractor = role == User.Role.CONTRACTOR
        return Response({
            "is_contractor": is_contractor,
            "has_profile": bool(prof),
            "identity_status": getattr(prof, "identity_status", None) if prof else None,
            "applied_at": getattr(prof, "created", None) if prof else None,
        })

    @action(detail=False, methods=["patch"], url_path="me/identity")
    def me_identity(self, request):
        prof, _ = ContractorProfile.objects.get_or_create(user=request.user)
        ser = ContractorIdentitySerializer(prof, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        prof.identity_status = ContractorProfile.VerifyStatus.PENDING
        ser.save()
        prof.save(update_fields=["identity_status"])
        return Response({"detail": "Identity submitted. Verification pending."}, status=200)


class ContractorAdminViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["get"], url_path="pending")
    def pending(self, request):
        qs = ContractorProfile.objects.filter(identity_status=ContractorProfile.VerifyStatus.PENDING).select_related("user")
        data = [{
            "user_id": p.user_id,
            "email": getattr(p.user, "email", ""),
            "phone": p.phone,
            "website": p.website,
            "years_experience": p.years_experience,
            "created": p.created,
        } for p in qs[:200]]
        return Response(data)

    @action(detail=True, methods=["get"], url_path="identity")
    def identity(self, request, pk=None):
        prof = get_object_or_404(ContractorProfile, user_id=pk)
        resp = {"identity_number": prof.identity_number or "", "has_document": bool(prof.identity_document)}
        return Response(resp)

    @action(detail=True, methods=["post"], url_path="approve")
    def approve(self, request, pk=None):
        prof = get_object_or_404(ContractorProfile, user_id=pk)
        prof.identity_status = ContractorProfile.VerifyStatus.APPROVED
        prof.save(update_fields=["identity_status"])
        return Response({"detail": "Approved"}, status=200)

    @action(detail=True, methods=["post"], url_path="reject")
    def reject(self, request, pk=None):
        prof = get_object_or_404(ContractorProfile, user_id=pk)
        prof.identity_status = ContractorProfile.VerifyStatus.REJECTED
        prof.identity_note = str(request.data.get("note") or "")
        prof.save(update_fields=["identity_status", "identity_note"])
        return Response({"detail": "Rejected"}, status=200)
