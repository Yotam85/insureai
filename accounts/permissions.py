from rest_framework.permissions import BasePermission
from .models import User

class IsContractor(BasePermission):
    def has_permission(self, request, view):
        u = getattr(request, "user", None)
        return bool(u and u.is_authenticated and getattr(u, "role", None) == User.Role.CONTRACTOR)

