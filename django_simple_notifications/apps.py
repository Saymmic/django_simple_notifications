from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_simple_notifications"

    def ready(self):
        try:
            from . import signals  # noqa F401
        except ImportError:
            pass
