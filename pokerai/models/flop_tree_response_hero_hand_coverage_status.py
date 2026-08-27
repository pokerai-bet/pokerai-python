from enum import Enum


class FlopTreeResponseHeroHandCoverageStatus(str, Enum):
    NOT_IN_REQUESTED_RANGE = "not_in_requested_range"
    REMOVED = "removed"
    REWEIGHTED = "reweighted"
    UNCHANGED = "unchanged"

    def __str__(self) -> str:
        return str(self.value)
