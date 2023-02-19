import datetime
import logging
import zoneinfo
from typing import Protocol

from .enums import NotificationStatus
from .factories import MediumFactoryProtocol
from .mappers import NotificationMapperProtocol
from .repositories import NotificationRepositoryProtocol
from .types import (
    AnyNotificationDTOType,
    ReturnSendNotificationType,
)

logger = logging.getLogger(__name__)


class NotificationServiceProtocol(Protocol):
    def send_notification(self, notification: AnyNotificationDTOType) -> ReturnSendNotificationType:
        ...


class NotificationService(NotificationServiceProtocol):
    def __init__(
        self,
        notification_mapper: NotificationMapperProtocol,
        notification_repository: NotificationRepositoryProtocol,
        medium_factory: MediumFactoryProtocol,
    ) -> None:
        self._notification_mapper = notification_mapper
        self._notification_repository = notification_repository
        self._medium_factory = medium_factory

    def send_notification(
        self, notification_dto: AnyNotificationDTOType
    ) -> ReturnSendNotificationType:
        notification = self._notification_mapper.to_entity(notification_dto=notification_dto)
        medium = self._medium_factory.create(notification=notification)

        logger.info("Sending notification %s", notification)
        try:
            medium.send_notification(notification=notification)
        except Exception as e:
            notification.status = NotificationStatus.ERROR
            logger.error("Notification sending error %s", notification, exc_info=e)
        else:
            notification.status = NotificationStatus.SENT
            notification.sent_at = datetime.datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
            logger.info("Notification sent successfully %s", notification)

        self._notification_repository.create(notification=notification)

        return {"notification_uuid": notification.uuid, "status": notification.status}
