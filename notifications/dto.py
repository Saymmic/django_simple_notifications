from dataclasses import dataclass


@dataclass
class DiscordWebhookNotificationDTO:
    subject: str
    body: str
    webhook: str


@dataclass
class EmailNotificationDTO:
    subject: str
    body: str
    to: str
    cc: list[str] | None = None
