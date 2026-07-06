from enum import Enum

class TurnProjectedRangeResponse200Type1SpotStatus(str, Enum):
    COMPUTING = "computing"

    def __str__(self) -> str:
        return str(self.value)
