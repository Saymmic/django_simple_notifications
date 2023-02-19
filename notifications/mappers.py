from typing import Protocol

from .dto import DiscordWebhookNotificationDTO, EmailNotificationDTO
from .entities.discord_webhook_notification import DiscordWebhookNotification
from .entities.email_notification import EmailNotification
from .types import AnyNotificationDTOType, AnyNotificationEntityType


class NotificationMapperProtocol(Protocol):
    @staticmethod
    def to_entity(notification_dto: AnyNotificationDTOType) -> AnyNotificationEntityType:
        ...


class NotificationMapper(NotificationMapperProtocol):
    @staticmethod
    def to_entity(notification_dto: AnyNotificationDTOType) -> AnyNotificationEntityType:
        if isinstance(notification_dto, DiscordWebhookNotificationDTO):
            return DiscordWebhookNotification(
                subject=notification_dto.subject,
                body=notification_dto.body,
                webhook=notification_dto.webhook,
            )
        if isinstance(notification_dto, EmailNotificationDTO):
            return EmailNotification(
                subject=notification_dto.subject,
                body=notification_dto.body,
                to=notification_dto.to,
                cc=notification_dto.cc,
            )
        else:
            raise NotImplementedError(f"No Mapper for {type(notification_dto)} implemented")
