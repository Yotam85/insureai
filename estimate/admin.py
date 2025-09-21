from django.contrib import admin
from django.db.models import Count
from .models import Project, EstimateJob, EstimateResult, Upload, ContractorLead, ContractorLeadResponse

class EstimateJobInline(admin.TabularInline):
    model = EstimateJob
    extra = 0
    fields = ("id", "status", "agent_kind", "instructions", "property_type", "work_grade", "created")
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
    list_display = ("id", "project", "project_seq", "title", "owner", "status", "agent_kind", "property_type", "work_grade", "created")
    list_filter  = ("status", "agent_kind", "property_type", "work_grade")
    search_fields = ("project_seq", "title", "instructions", "claim_number", "project__name", "project__zip", "owner__email")
    autocomplete_fields = ("project", "owner")
    date_hierarchy = "created"
    list_select_related = ("project", "owner")

@admin.register(EstimateResult)
class EstimateResultAdmin(admin.ModelAdmin):
    list_display = ("job_id", "owner", "total_cost", "created", "has_pdf")
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


class ContractorLeadResponseInline(admin.TabularInline):
    model = ContractorLeadResponse
    extra = 0
    autocomplete_fields = ("contractor",)
    readonly_fields = ("created", "updated")


@admin.register(ContractorLead)
class ContractorLeadAdmin(admin.ModelAdmin):
    list_display = ("id", "job", "status", "total_cost", "posted_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("headline", "job__instructions", "job__project__name")
    autocomplete_fields = ("job", "result")
    readonly_fields = ("posted_at", "updated_at")
    inlines = [ContractorLeadResponseInline]


@admin.register(ContractorLeadResponse)
class ContractorLeadResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "lead", "contractor", "decision", "created")
    list_filter = ("decision",)
    search_fields = ("lead__headline", "contractor__email", "contractor__username")
    autocomplete_fields = ("lead", "contractor")
    readonly_fields = ("created", "updated")
