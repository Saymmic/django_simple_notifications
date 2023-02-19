from __future__ import annotations

import datetime
from typing import Final
from uuid import UUID

from ..enums import NotificationStatus
from .notification import Notification


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
        super().__init__(uuid=uuid, status=status, created_at=created_at, sent_at=sent_at)
        self.subject = subject
        self.body = body
        self.to = to
        self.cc = cc
