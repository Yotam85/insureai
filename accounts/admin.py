from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, LoginCode, ContractorProfile, ContractorTag

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("id", "username", "email", "role", "is_staff", "is_active")
    search_fields = ("username", "email")

@admin.register(LoginCode)
class LoginCodeAdmin(admin.ModelAdmin):
    list_display = ("email", "guest_key", "created_at", "expires_at", "attempts", "used_at")
    search_fields = ("email", "guest_key")

@admin.register(ContractorTag)
class ContractorTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(ContractorProfile)
class ContractorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "website", "years_experience", "identity_status", "created")
    list_filter = ("identity_status",)
    search_fields = ("user__email", "user__username", "phone", "website")
    readonly_fields = ("created", "updated")
