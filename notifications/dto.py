from dataclasses import dataclass


@dataclass
class DiscordWebhookNotificationDTO:
    subject: str
    body: str
    webhook: str
