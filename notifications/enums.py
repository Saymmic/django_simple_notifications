from enum import StrEnum, auto


class NotificationStatus(StrEnum):
    CREATED = auto()
    SENDING = auto()
    SENT = auto()
    ERROR = auto()

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(i.name.lower(), i.value.lower()) for i in cls]


class NotificationType(StrEnum):
    DISCORD_WEBHOOK = auto()

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(i.name.lower(), i.value.lower()) for i in cls]
