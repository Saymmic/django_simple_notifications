import uuid

from django.db import models

from .enums import NotificationStatus


class Notification(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=32)
    status = models.CharField(max_length=32, choices=NotificationStatus.choices())
    created_at = models.DateTimeField()
    sent_at = models.DateTimeField(null=True, blank=True)
    details = models.JSONField(null=True, blank=True)
