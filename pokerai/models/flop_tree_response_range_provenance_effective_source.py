from enum import Enum


class FlopTreeResponseRangeProvenanceEffectiveSource(str, Enum):
    PERSISTED_SOLVE_CONFIG = "persisted_solve_config"

    def __str__(self) -> str:
        return str(self.value)
