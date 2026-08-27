from enum import Enum


class FlopNodeResponse422Error(str, Enum):
    HAND_NOT_IN_EFFECTIVE_RANGE = "hand_not_in_effective_range"

    def __str__(self) -> str:
        return str(self.value)
