from typing import TypedDict

from .dto import DiscordWebhookNotificationDTO, EmailNotificationDTO
from .entities import DiscordWebhookNotification, EmailNotification

AnyNotificationEntityType = DiscordWebhookNotification | EmailNotification
AnyNotificationDTOType = DiscordWebhookNotificationDTO | EmailNotificationDTO


class ReturnSendNotificationType(TypedDict):
    notification_uuid: str
    status: str
