from typing import TypedDict

from .dto import DiscordWebhookNotificationDTO, EmailNotificationDTO
from .entities.discord_webhook_notification import DiscordWebhookNotification
from .entities.email_notification import EmailNotification

AnyNotificationEntityType = DiscordWebhookNotification | EmailNotification
AnyNotificationDTOType = DiscordWebhookNotificationDTO | EmailNotificationDTO


class ReturnSendNotificationType(TypedDict):
    notification_uuid: str
    status: str
