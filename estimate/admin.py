from django.contrib import admin
from django.db.models import Count
from .models import Project, EstimateJob, EstimateResult, Upload

class EstimateJobInline(admin.TabularInline):
    model = EstimateJob
    extra = 0
    fields = ("id", "status", "agent_kind", "instructions", "property_type", "damage_type", "created")
    readonly_fields = ("id", "created")
    show_change_link = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "zip", "owner", "guest_key", "job_count", "created")
    list_filter  = ("zip", "owner")
    search_fields = ("name", "zip", "guest_key", "owner__email", "owner__username")
    date_hierarchy = "created"
    ordering = ("-created", "-id")
    inlines = [EstimateJobInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_job_count=Count("jobs"))

    @admin.display(ordering="_job_count", description="Jobs")
    def job_count(self, obj):
        return getattr(obj, "_job_count", 0)

@admin.register(EstimateJob)
class EstimateJobAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "project_seq", "title", "owner", "status", "agent_kind", "property_type", "damage_type", "created")
    list_filter  = ("status", "agent_kind", "property_type", "damage_type")
    search_fields = ("project_seq", "title", "instructions", "claim_number", "project__name", "project__zip", "owner__email")
    autocomplete_fields = ("project", "owner")
    date_hierarchy = "created"
    list_select_related = ("project", "owner")

@admin.register(EstimateResult)
class EstimateResultAdmin(admin.ModelAdmin):
    list_display = ("job_id", "owner", "premium", "created", "has_pdf")
    search_fields = ("job__instructions", "owner__email")
    list_select_related = ("job", "owner")

    @admin.display(boolean=True, description="PDF")
    def has_pdf(self, obj):
        return bool(obj.pdf_file)

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "mime", "owner", "guest_key", "job")
    search_fields = ("file", "mime", "guest_key", "owner__email")
    list_filter = ("mime",)
    autocomplete_fields = ("owner", "job")
