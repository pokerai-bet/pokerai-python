from enum import Enum


class SolverScheduleResponseStatus(str, Enum):
    BUSY = "busy"
    COMPUTING = "computing"
    QUERYABLE = "queryable"

    def __str__(self) -> str:
        return str(self.value)
