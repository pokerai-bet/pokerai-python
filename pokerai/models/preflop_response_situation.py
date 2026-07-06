from enum import Enum

class PreflopResponseSituation(str, Enum):
    LIMP = "Limp"
    RAISE = "Raise"
    RFI = "RFI"
    VALUE_3 = "3-Bet"
    VALUE_4 = "4-Bet"
    VALUE_5 = "5-Bet"

    def __str__(self) -> str:
        return str(self.value)
