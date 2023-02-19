from __future__ import annotations

import datetime
import zoneinfo
from typing import Final
from uuid import UUID, uuid4

from .enums import NotificationStatus


class Notification:
    @property
    def TYPE(self) -> str:
        raise NotImplementedError()

    def __init__(
        self,
        uuid: UUID | None = None,
        status: NotificationStatus = NotificationStatus.CREATED,
        created_at: datetime.datetime | None = None,
        sent_at: datetime.datetime | None = None,
    ) -> None:
        self.uuid = uuid or uuid4()
        self.status = status
        self.created_at = created_at or datetime.datetime.now(
            tz=zoneinfo.ZoneInfo("UTC")
        )
        self.sent_at: datetime.datetime | None = sent_at

    def __str__(self) -> str:
        return (
            f"UUID: {self.uuid} type: {self.TYPE} status: {self.status} created_at: {self.created_at.isoformat()} "
            f"sent_at: {self.sent_at.isoformat() if self.sent_at else ''}"
        )


class DiscordWebhookNotification(Notification):
    TYPE: Final[str] = "discord_webhook"

    def __init__(
        self,
        subject: str,
        body: str,
        webhook: str,
        uuid: UUID | None = None,
        status: NotificationStatus = NotificationStatus.CREATED,
        created_at: datetime.datetime | None = None,
        sent_at: datetime.datetime | None = None,
    ) -> None:
        super().__init__(
            uuid=uuid, status=status, created_at=created_at, sent_at=sent_at
        )
        self.subject = subject
        self.body = body
        self.webhook = webhook


class EmailNotification(Notification):
    TYPE: Final[str] = "email"

    def __init__(
        self,
        subject: str,
        body: str,
        to: str,
        cc: list[str] | None,
        uuid: UUID | None = None,
        status: NotificationStatus = NotificationStatus.CREATED,
        created_at: datetime.datetime | None = None,
        sent_at: datetime.datetime | None = None,
    ) -> None:
        super().__init__(
            uuid=uuid, status=status, created_at=created_at, sent_at=sent_at
        )
        self.subject = subject
        self.body = body
        self.to = to
        self.cc = cc
