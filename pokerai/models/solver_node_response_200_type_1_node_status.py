from enum import Enum

class SolverNodeResponse200Type1NodeStatus(str, Enum):
    AVAILABLE = "available"
    COMPUTING = "computing"
    ERROR = "error"
    EXPIRED = "expired"
    QUERYABLE = "queryable"

    def __str__(self) -> str:
        return str(self.value)
