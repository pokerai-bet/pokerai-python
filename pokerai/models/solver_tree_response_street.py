from enum import Enum


class SolverTreeResponseStreet(str, Enum):
    FLOP = "flop"
    RIVER = "river"
    TURN = "turn"

    def __str__(self) -> str:
        return str(self.value)
