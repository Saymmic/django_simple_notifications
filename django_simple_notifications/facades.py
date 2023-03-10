from typing import Protocol

from .mappers import NotificationMapper
from .repositories import DjangoNotificationRepository
from .services import NotificationService, NotificationServiceProtocol
from .types import AnyNotificationDTOType, ReturnSendNotificationType


class NotificationFacadeProtocol(Protocol):
    def send_notification(
        self, notification_dto: AnyNotificationDTOType
    ) -> ReturnSendNotificationType:
        ...


class NotificationFacade(NotificationFacadeProtocol):
    def __init__(self, notification_service: NotificationServiceProtocol | None = None):
        self.notification_service = notification_service or NotificationService(
            notification_mapper=NotificationMapper(),
            notification_repository=DjangoNotificationRepository(),
        )

    def send_notification(
        self, notification_dto: AnyNotificationDTOType
    ) -> ReturnSendNotificationType:
        return self.notification_service.send_notification(notification_dto=notification_dto)
