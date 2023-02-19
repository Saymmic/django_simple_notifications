from typing import Protocol

from .entities import DiscordWebhookNotification, EmailNotification
from .mediums import DiscordWebhookMedium, EmailMedium, MediumProtocol
from .types import AnyNotificationEntityType


class MediumFactoryProtocol(Protocol):
    @classmethod
    def create(cls, notification: AnyNotificationEntityType) -> MediumProtocol:
        ...


class MediumFactory(MediumFactoryProtocol):
    @classmethod
    def create(cls, notification: AnyNotificationEntityType) -> MediumProtocol:
        if isinstance(notification, DiscordWebhookNotification):
            return DiscordWebhookMedium()
        if isinstance(notification, EmailNotification):
            return EmailMedium()
        else:
            raise NotImplementedError(
                f"There is no medium implemented for {type(notification)}"
            )
