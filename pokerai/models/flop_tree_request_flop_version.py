from enum import Enum

class FlopTreeRequestFlopVersion(str, Enum):
    VALUE_0 = "6max"
    VALUE_1 = "6max_RC_100bb_200NL"
    VALUE_2 = "6max_RC_100bb_100NL"
    VALUE_3 = "6max_RC_40bb"

    def __str__(self) -> str:
        return str(self.value)
