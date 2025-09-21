from django.apps import AppConfig


class EstimateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estimate'

    def ready(self):  # pragma: no cover - import signals for side effects
        try:
            import estimate.signals  # noqa: F401
        except Exception:
            # Avoid hard crash if migrations aren't ready yet
            pass
