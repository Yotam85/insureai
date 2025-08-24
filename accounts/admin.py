from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, LoginCode

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")

@admin.register(LoginCode)
class LoginCodeAdmin(admin.ModelAdmin):
    list_display = ("email", "guest_key", "created_at", "expires_at", "attempts", "used_at")
    search_fields = ("email", "guest_key")
