from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.preflop_range_response_200_range_additional_property import (
        PreflopRangeResponse200RangeAdditionalProperty,
    )


T = TypeVar("T", bound="PreflopRangeResponse200Range")


@_attrs_define
class PreflopRangeResponse200Range:
    """hand type (AA / AKs / AKo) -> {fold, call, raise}; 169 entries, each summing to ~1"""

    additional_properties: dict[str, "PreflopRangeResponse200RangeAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_response_200_range_additional_property import (
            PreflopRangeResponse200RangeAdditionalProperty,
        )

        d = dict(src_dict)
        preflop_range_response_200_range = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PreflopRangeResponse200RangeAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        preflop_range_response_200_range.additional_properties = additional_properties
        return preflop_range_response_200_range

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "PreflopRangeResponse200RangeAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "PreflopRangeResponse200RangeAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
