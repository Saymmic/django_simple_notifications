from typing import TypedDict

from .dto import DiscordWebhookNotificationDTO
from .entities import DiscordWebhookNotification

AnyNotificationEntityType = DiscordWebhookNotification
AnyNotificationDTOType = DiscordWebhookNotificationDTO


class ReturnSendNotificationType(TypedDict):
    notification_uuid: str
    status: str
