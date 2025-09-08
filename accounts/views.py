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
from rest_framework.decorators import api_view, permission_classes

from .models import LoginCode
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
    try:
        send_mail(
            "Your Estimai sign-in code",
            f"Your sign-in code is: {code}\n\nThis code expires in {CODE_TTL_MIN} minutes.",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        logger.exception("Failed to send email")
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
