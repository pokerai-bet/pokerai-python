from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges_additional_property import (
        PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty,
    )


T = TypeVar("T", bound="PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges")


@_attrs_define
class PreflopRangeResponse200FlopPruningGuaranteesContinuationType0Ranges:
    """ """

    additional_properties: dict[
        str, "PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges_additional_property import (
            PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty,
        )

        d = dict(src_dict)
        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges.additional_properties = (
            additional_properties
        )
        return preflop_range_response_200_flop_pruning_guarantees_continuation_type_0_ranges

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> "PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: "PreflopRangeResponse200FlopPruningGuaranteesContinuationType0RangesAdditionalProperty"
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
