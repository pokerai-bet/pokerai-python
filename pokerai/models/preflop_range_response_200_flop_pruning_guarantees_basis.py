from enum import Enum


class PreflopRangeResponse200FlopPruningGuaranteesBasis(str, Enum):
    SERVED_ARTIFACTS = "served_artifacts"

    def __str__(self) -> str:
        return str(self.value)
