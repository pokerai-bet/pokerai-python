from enum import Enum


class PreflopRangeResponse200FlopPruningGuaranteesStatus(str, Enum):
    AWAITING_TERMINAL_PREFLOP_ACTION = "awaiting_terminal_preflop_action"
    COMPLETE = "complete"
    INCOMPLETE_COVERAGE = "incomplete_coverage"

    def __str__(self) -> str:
        return str(self.value)
