# accounts/management/commands/cleanup_logincodes.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import LoginCode

class BaseCommand(BaseCommand):
    help = "Delete expired login codes"

    def handle(self, *args, **kwargs):
        n = LoginCode.objects.filter(expires_at__lt=timezone.now()).delete()
        self.stdout.write(f"Deleted: {n}")
