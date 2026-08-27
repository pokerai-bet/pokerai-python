from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges import (
        PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges,
    )
    from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario import (
        PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario,
    )


T = TypeVar("T", bound="PreflopRangeResponse200FlopPruningGuaranteesContinuationType0")


@_attrs_define
class PreflopRangeResponse200FlopPruningGuaranteesContinuationType0:
    """
    Attributes:
        action (Union[Unset, str]):
        scenario (Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario]):
        canonical_board_count (Union[Unset, int]):
        ranges (Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges]):
    """

    action: Union[Unset, str] = UNSET
    scenario: Union[Unset, "PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario"] = UNSET
    canonical_board_count: Union[Unset, int] = UNSET
    ranges: Union[Unset, "PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        scenario: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scenario, Unset):
            scenario = self.scenario.to_dict()

        canonical_board_count = self.canonical_board_count

        ranges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = self.ranges.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if canonical_board_count is not UNSET:
            field_dict["canonical_board_count"] = canonical_board_count
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges import (
            PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges,
        )
        from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario import (
            PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario,
        )

        d = dict(src_dict)
        action = d.pop("action", UNSET)

        _scenario = d.pop("scenario", UNSET)
        scenario: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario]
        if isinstance(_scenario, Unset):
            scenario = UNSET
        else:
            scenario = PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario.from_dict(_scenario)

        canonical_board_count = d.pop("canonical_board_count", UNSET)

        _ranges = d.pop("ranges", UNSET)
        ranges: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges]
        if isinstance(_ranges, Unset):
            ranges = UNSET
        else:
            ranges = PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges.from_dict(_ranges)

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0 = cls(
            action=action,
            scenario=scenario,
            canonical_board_count=canonical_board_count,
            ranges=ranges,
        )

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0.additional_properties = d
        return preflop_range_response_200_flop_pruning_guarantees_continuation_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
