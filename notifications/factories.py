from typing import Protocol

from .entities import DiscordWebhookNotification
from .mediums import DiscordWebhookMedium, MediumProtocol
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
        else:
            raise NotImplementedError(f"There is no medium implemented for {type(notification)}")
