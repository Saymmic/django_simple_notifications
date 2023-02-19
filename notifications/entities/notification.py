"""
Entities should not depend on anything. But business logic in this project is laser focused
on sending notifications. Implementing send logic directly on the entity saves us lot
of complexity.

For more details compare it to older commits.
"""
from __future__ import annotations

import datetime
import zoneinfo
from uuid import UUID, uuid4

from ..enums import NotificationStatus


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
        self.created_at = created_at or datetime.datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
        self.sent_at: datetime.datetime | None = sent_at

    def __str__(self) -> str:
        return (
            f"UUID: {self.uuid} "
            f"type: {self.TYPE} "
            f"status: {self.status} "
            f"created_at: {self.created_at.isoformat()} "
            f"sent_at: {self.sent_at.isoformat() if self.sent_at else ''}"
        )

    def send(self) -> None:
        raise NotImplementedError()
