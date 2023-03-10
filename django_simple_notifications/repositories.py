from typing import Protocol

from .models import Notification as DjangoNotification
from .types import AnyNotificationEntityType


class NotificationRepositoryProtocol(Protocol):
    def create(self, notification: AnyNotificationEntityType) -> None:
        ...


class DjangoNotificationRepository(NotificationRepositoryProtocol):
    def _get_details(self, notification: AnyNotificationEntityType) -> dict:
        """
        Details are Notification Type specific fields.
        So everything that it is non-standard notification field.
        """
        details = {k: v for k, v in vars(notification).items() if not k.startswith("_")}

        for key in ["status", "created_at", "sent_at", "uuid"]:
            details.pop(key, None)

        return details

    def create(self, notification: AnyNotificationEntityType) -> None:
        django_notification = DjangoNotification(
            uuid=notification.uuid,
            type=notification.TYPE,
            status=notification.status,
            created_at=notification.created_at,
            sent_at=notification.sent_at,
            details=self._get_details(notification=notification),
        )
        django_notification.save()
