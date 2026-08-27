from enum import Enum


class FlopTreeResponseRangeProvenancePolicyAuditStatus(str, Enum):
    MISMATCH = "mismatch"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
