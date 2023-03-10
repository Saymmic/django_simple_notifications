from dataclasses import dataclass
from email.mime.base import MIMEBase


@dataclass
class DiscordWebhookNotificationDTO:
    subject: str
    body: str
    webhook: str


@dataclass
class EmailNotificationDTO:
    subject: str
    body: str
    sender_email: str
    recipient_email: str
    cc: list[str] | None = None
    bcc: list[str] | None = None
    attachments: list[MIMEBase] | None = None
