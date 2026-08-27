from enum import Enum


class PreflopRequestPreflopActionsItemAction(str, Enum):
    BIG_BLIND = "big blind"
    CALL = "call"
    FOLD = "fold"
    RAISE = "raise"
    SMALL_BLIND = "small blind"

    def __str__(self) -> str:
        return str(self.value)
