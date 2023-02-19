import asyncio
from typing import Protocol

import aiohttp
import discord

from .dto import DiscordWebhookNotificationDTO
from .types import AnyNotificationEntityType


class MediumProtocol(Protocol):
    def send_notification(self, notification: AnyNotificationEntityType) -> None:
        ...


class DiscordWebhookMedium(MediumProtocol):
    def send_notification(self, notification: AnyNotificationEntityType) -> None:
        asyncio.run(self._send_notification(notification=notification))

    async def _send_notification(
        self, notification: DiscordWebhookNotificationDTO
    ) -> None:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(notification.webhook, session=session)
            embed = discord.Embed(
                title=notification.subject, description=notification.body
            )

            await webhook.send(embed=embed)


class EmailMedium(MediumProtocol):
    def send_notification(self, notification: AnyNotificationEntityType) -> None:
        pass
