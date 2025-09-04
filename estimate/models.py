# estimate/models.py
import uuid

from django.conf import settings
from django.db import models


# estimate/models.py
class Upload(models.Model):
    file      = models.FileField(upload_to="%Y/%m/")
    guest_key  = models.CharField(max_length=64, null=True, blank=True, db_index=True)
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
    guest_key  = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,   # if the user is ever deleted
        null=True, blank=True        # ←  allow NULL
    
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

    # 32-char hex UUID (no hyphens) fits CharField(32)
    claim_number = models.CharField(
        max_length=32,
        default=uuid.uuid4().hex,   # callable evaluated for each new row
        null=True, blank=True,      # keep nullable while you prototype
        # unique=True,              # re-enable later after data back-fill
    )

    PROPERTY_CHOICES = [("res", "Residential"), ("com", "Commercial")]
    property_type = models.CharField(max_length=3, choices=PROPERTY_CHOICES,
                                     null=True, blank=True)

    DAMAGE_CHOICES = [("water", "Water"), ("fire", "Fire"), ("wind", "Wind")]
    damage_type = models.CharField(max_length=5, choices=DAMAGE_CHOICES,
                                   null=True, blank=True)

    status  = models.CharField(max_length=12, default="PENDING")
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Job {self.pk or '∅'} • {self.status}"


# estimate/models.py (only the EstimateResult bits)
from django.conf import settings
from django.db import models

class EstimateResult(models.Model):
    # ← primary key is job (NO separate id field)
    job = models.OneToOneField(
        'EstimateJob',
        on_delete=models.CASCADE,
        related_name='estimateresult',
        primary_key=True,
    )
    owner     = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    guest_key = models.CharField(max_length=64, blank=True, null=True)
    raw_json  = models.JSONField(default=dict)
    premium   = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    pdf_file  = models.FileField(upload_to="estimates/", null=True, blank=True)
    created   = models.DateTimeField(auto_now_add=True)




# estimate/models.py (snippets)
from django.conf import settings

owner = models.ForeignKey(
    settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="…"
)
