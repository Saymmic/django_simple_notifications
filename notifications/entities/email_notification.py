from __future__ import annotations

import datetime
from email.mime.base import MIMEBase
from typing import Final
from uuid import UUID

from django.core.mail import EmailMessage

from ..enums import NotificationStatus
from .notification import Notification


class EmailNotification(Notification):
    TYPE: Final[str] = "email"

    def __init__(
        self,
        subject: str,
        body: str,
        sender_email: str,
        recipient_email: str,
        cc: list[str] | None = None,
        bcc: list[str] | None = None,
        attachments: list[MIMEBase] | None = None,
        uuid: UUID | None = None,
        status: NotificationStatus = NotificationStatus.CREATED,
        created_at: datetime.datetime | None = None,
        sent_at: datetime.datetime | None = None,
    ) -> None:
        super().__init__(uuid=uuid, status=status, created_at=created_at, sent_at=sent_at)
        self.subject = subject
        self.body = body
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.cc = cc
        self.bcc = bcc
        self.attachments = attachments

    def send(self) -> None:
        EmailMessage(
            subject=self.subject,
            body=self.body,
            from_email=self.sender_email,
            to=self.recipient_email,
            bcc=self.bcc,
            attachments=self.attachments,
            cc=self.cc,
        ).send()
