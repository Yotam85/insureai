from __future__ import annotations
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.postgres.fields import ArrayField
import os

class User(AbstractUser):
    class Role(models.TextChoices):
        USER = "user", "User"
        CONTRACTOR = "contractor", "Contractor"
        ADJUSTER = "adjuster", "Adjuster"

    email = models.EmailField("email address", unique=True)
    role = models.CharField(max_length=24, choices=Role.choices, default=Role.USER)

    def __str__(self) -> str:
        return self.username or self.email or f"user-{self.pk}"

class LoginCode(models.Model):
    user       = models.ForeignKey("accounts.User", null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="login_codes")
    email      = models.EmailField(db_index=True)
    code_hash  = models.CharField(max_length=128)
    guest_key  = models.CharField(max_length=64, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    attempts   = models.PositiveSmallIntegerField(default=0)
    used_at    = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=["email", "expires_at"])]

    @property
    def is_expired(self) -> bool:
        return timezone.now() >= self.expires_at

    @property
    def is_used(self) -> bool:
        return self.used_at is not None


# ---- Contractor profile & tags ----

# Private media root (not publicly served by web server)
PRIVATE_MEDIA_ROOT = getattr(settings, "PRIVATE_MEDIA_ROOT", os.path.join(settings.BASE_DIR, "private_media"))
private_storage = FileSystemStorage(location=PRIVATE_MEDIA_ROOT, base_url=None)

class ContractorTag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

try:
    from fernet_fields import EncryptedTextField  # type: ignore
except Exception:
    # Fallback if package missing; not encrypted but keeps API working in dev
    class EncryptedTextField(models.TextField):
        pass

class ContractorProfile(models.Model):
    class VerifyStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    YEARS_EXPERIENCE_CHOICES = (
        ("<1", "Less than 1 year"),
        ("1-3", "1-3 years"),
        ("3-5", "3-5 years"),
        ("5-10", "5-10 years"),
        ("10+", "10+ years"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="contractor_profile")

    # Public profile
    full_name = models.CharField(max_length=160, blank=True, default="")
    company = models.CharField(max_length=160, blank=True, default="")
    phone = models.CharField(max_length=32, blank=True, default="")
    website = models.URLField(blank=True, default="")
    license_number = models.CharField(max_length=80, blank=True, default="")
    trades = ArrayField(models.CharField(max_length=80), default=list, blank=True)
    zip_codes = models.TextField(blank=True, default="")
    years_experience = models.CharField(max_length=8, choices=YEARS_EXPERIENCE_CHOICES, blank=True, default="")
    insured = models.BooleanField(default=False)
    bonded = models.BooleanField(default=False)
    project_sizes = ArrayField(models.CharField(max_length=80), default=list, blank=True)
    project_types = ArrayField(models.CharField(max_length=80), default=list, blank=True)
    availability = models.CharField(max_length=160, blank=True, default="")
    how_heard = models.CharField(max_length=160, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    attachment = models.FileField(upload_to="contractors/applications/%Y/%m/", storage=private_storage, blank=True, null=True)
    photo = models.ImageField(upload_to="contractors/photos/%Y/%m/", blank=True, null=True)
    tags = models.ManyToManyField(ContractorTag, blank=True, related_name="contractors")
    address_line1 = models.CharField(max_length=160, blank=True)
    address_line2 = models.CharField(max_length=160, blank=True)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=40, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=2, blank=True)
    bio = models.TextField(blank=True)

    # Identity (admin-only / private)
    identity_status = models.CharField(max_length=16, choices=VerifyStatus.choices, default=VerifyStatus.PENDING)
    identity_note = models.TextField(blank=True)
    identity_number = EncryptedTextField(blank=True, null=True)
    identity_document = models.FileField(upload_to="contractors/id_docs/%Y/%m/", storage=private_storage, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ContractorProfile({self.user_id})"
