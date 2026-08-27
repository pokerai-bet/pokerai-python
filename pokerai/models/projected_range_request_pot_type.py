from enum import Enum


class ProjectedRangeRequestPotType(str, Enum):
    LIMP = "LIMP"
    SRP = "SRP"
    VALUE_1 = "3BET"
    VALUE_2 = "4BET"

    def __str__(self) -> str:
        return str(self.value)
