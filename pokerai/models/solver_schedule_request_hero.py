from enum import Enum

class SolverScheduleRequestHero(str, Enum):
    IP = "IP"
    OOP = "OOP"

    def __str__(self) -> str:
        return str(self.value)
