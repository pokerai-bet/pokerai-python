from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty")


@_attrs_define
class PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty:
    """
    Attributes:
        source_action (Union[Unset, str]):
        position (Union[Unset, str]):
        always_removed (Union[Unset, list[str]]):
    """

    source_action: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    always_removed: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_action = self.source_action

        position = self.position

        always_removed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.always_removed, Unset):
            always_removed = self.always_removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_action is not UNSET:
            field_dict["source_action"] = source_action
        if position is not UNSET:
            field_dict["position"] = position
        if always_removed is not UNSET:
            field_dict["always_removed"] = always_removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_action = d.pop("source_action", UNSET)

        position = d.pop("position", UNSET)

        always_removed = cast(list[str], d.pop("always_removed", UNSET))

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges_additional_property = cls(
            source_action=source_action,
            position=position,
            always_removed=always_removed,
        )

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges_additional_property.additional_properties = d
        return preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges_additional_property

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
