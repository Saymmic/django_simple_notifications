# from dataclasses import dataclass
# import importlib
#
# from celery import Celery
# from django.conf import settings

# @dataclass
# class DiscordWebhookSettings:
#     DISCORD_WEBHOOK: str | None


# discord_webhook_settings = DiscordWebhookSettings(
#     DISCORD_WEBHOOK=getattr(settings, "DISCORD_WEBHOOK", None)
# )

# Import celery app in order to add send notification task.
