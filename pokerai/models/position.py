from enum import Enum


class Position(str, Enum):
    BB = "BB"
    BTN = "BTN"
    CO = "CO"
    MP = "MP"
    SB = "SB"
    UTG = "UTG"

    def __str__(self) -> str:
        return str(self.value)
