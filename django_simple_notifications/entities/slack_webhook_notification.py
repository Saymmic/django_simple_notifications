from __future__ import annotations

import datetime
from typing import Final
from uuid import UUID

import httpx

from ..enums import NotificationStatus
from .notification import Notification


class SlackWebhookNotification(Notification):
    TYPE: Final[str] = "slack_webhook"

    def __init__(
        self,
        text: str,
        webhook: str,
        blocks: list[dict] = None,
        uuid: UUID | None = None,
        status: NotificationStatus = NotificationStatus.CREATED,
        created_at: datetime.datetime | None = None,
        sent_at: datetime.datetime | None = None,
    ) -> None:
        super().__init__(uuid=uuid, status=status, created_at=created_at, sent_at=sent_at)
        self.text = text
        self.blocks = blocks
        self.webhook = webhook

    def send(self) -> None:
        message_payload = {"text": self.text}

        if self.blocks is not None:
            message_payload["blocks"] = self.blocks

        httpx.post(self.webhook, json=message_payload)
