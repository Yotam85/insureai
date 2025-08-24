# estimate/admin.py
from django.contrib import admin
from .models import EstimateJob, Upload, EstimateResult


class UploadInline(admin.TabularInline):
    model = Upload
    fields = ("file", "mime")
    readonly_fields = fields
    extra = 0            # no empty rows


@admin.register(EstimateJob)
class EstimateJobAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "status", "property_type", "damage_type")
    inlines       = (UploadInline,)


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "mime", "job")   # quick reverse lookup


@admin.register(EstimateResult)
class EstimateResultAdmin(admin.ModelAdmin):
    list_display = ("job", "premium")
