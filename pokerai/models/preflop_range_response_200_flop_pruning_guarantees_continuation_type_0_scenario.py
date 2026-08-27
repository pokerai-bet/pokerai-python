from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario_preflop_type import (
    PreflopRangeResponse200FlopPruningGuaranteesContinuationType0ScenarioPreflopType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario")


@_attrs_define
class PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Scenario:
    """
    Attributes:
        preflop_type (Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0ScenarioPreflopType]):
        raiser (Union[Unset, str]):
        caller (Union[Unset, str]):
    """

    preflop_type: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0ScenarioPreflopType] = UNSET
    raiser: Union[Unset, str] = UNSET
    caller: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preflop_type: Union[Unset, str] = UNSET
        if not isinstance(self.preflop_type, Unset):
            preflop_type = self.preflop_type.value

        raiser = self.raiser

        caller = self.caller

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preflop_type is not UNSET:
            field_dict["preflop_type"] = preflop_type
        if raiser is not UNSET:
            field_dict["raiser"] = raiser
        if caller is not UNSET:
            field_dict["caller"] = caller

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _preflop_type = d.pop("preflop_type", UNSET)
        preflop_type: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0ScenarioPreflopType]
        if isinstance(_preflop_type, Unset):
            preflop_type = UNSET
        else:
            preflop_type = PreflopRangeResponse200FlopPruningGuaranteesContinuationType0ScenarioPreflopType(
                _preflop_type
            )

        raiser = d.pop("raiser", UNSET)

        caller = d.pop("caller", UNSET)

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario = cls(
            preflop_type=preflop_type,
            raiser=raiser,
            caller=caller,
        )

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario.additional_properties = d
        return preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_scenario

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
