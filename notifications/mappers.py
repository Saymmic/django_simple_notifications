from typing import Protocol

from .dto import DiscordWebhookNotificationDTO
from .entities import DiscordWebhookNotification
from .types import (
    AnyNotificationDTOType,
    AnyNotificationEntityType,
)


class NotificationMapperProtocol(Protocol):
    @staticmethod
    def to_dto(notification: AnyNotificationEntityType) -> AnyNotificationDTOType:
        ...

    @staticmethod
    def to_entity(notification_dto: AnyNotificationDTOType) -> AnyNotificationEntityType:
        ...


class DiscordWebhookNotificationMapper(NotificationMapperProtocol):
    @staticmethod
    def to_dto(notification: DiscordWebhookNotification) -> DiscordWebhookNotificationDTO:
        return DiscordWebhookNotificationDTO(
            subject=notification.subject, body=notification.body, webhook=notification.webhook
        )

    @staticmethod
    def to_entity(notification_dto: DiscordWebhookNotificationDTO) -> DiscordWebhookNotification:
        return DiscordWebhookNotification(
            subject=notification_dto.subject,
            body=notification_dto.body,
            webhook=notification_dto.webhook,
        )


class NotificationMapper(NotificationMapperProtocol):
    @staticmethod
    def to_dto(notification: AnyNotificationEntityType) -> AnyNotificationDTOType:
        if isinstance(notification, DiscordWebhookNotification):
            return DiscordWebhookNotificationMapper.to_dto(notification=notification)
        else:
            raise NotImplementedError(f"No Mapper for {type(notification)} implemented")

    @staticmethod
    def to_entity(notification_dto: AnyNotificationDTOType) -> AnyNotificationEntityType:
        if isinstance(notification_dto, DiscordWebhookNotificationDTO):
            return DiscordWebhookNotificationMapper.to_entity(notification_dto=notification_dto)
        else:
            raise NotImplementedError(f"No Mapper for {type(notification_dto)} implemented")
