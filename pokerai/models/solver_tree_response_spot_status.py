from enum import Enum


class SolverTreeResponseSpotStatus(str, Enum):
    AVAILABLE = "available"
    COMPUTING = "computing"
    EXPIRED = "expired"
    NO_NODES = "no_nodes"
    QUERYABLE = "queryable"

    def __str__(self) -> str:
        return str(self.value)
