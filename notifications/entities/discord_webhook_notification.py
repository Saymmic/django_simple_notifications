from __future__ import annotations

import asyncio
import datetime
from typing import Final
from uuid import UUID

import aiohttp
import discord

from ..enums import NotificationStatus
from .notification import Notification


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
        super().__init__(uuid=uuid, status=status, created_at=created_at, sent_at=sent_at)
        self.subject = subject
        self.body = body
        self.webhook = webhook

    def send(self) -> None:
        asyncio.run(self._send_notification())

    async def _send_notification(self) -> None:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(self.webhook, session=session)
            embed = discord.Embed(title=self.subject, description=self.body)

            await webhook.send(embed=embed)
