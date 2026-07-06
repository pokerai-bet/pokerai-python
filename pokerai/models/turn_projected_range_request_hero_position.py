from enum import Enum

class TurnProjectedRangeRequestHeroPosition(str, Enum):
    IP = "ip"
    OOP = "oop"

    def __str__(self) -> str:
        return str(self.value)
