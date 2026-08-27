from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopTreeResponseRangesEffective")


@_attrs_define
class FlopTreeResponseRangesEffective:
    """
    Attributes:
        oop (Union[Unset, str]): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1,
            default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
        ip (Union[Unset, str]): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1,
            default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
    """

    oop: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oop = self.oop

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oop is not UNSET:
            field_dict["oop"] = oop
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oop = d.pop("oop", UNSET)

        ip = d.pop("ip", UNSET)

        flop_tree_response_ranges_effective = cls(
            oop=oop,
            ip=ip,
        )

        flop_tree_response_ranges_effective.additional_properties = d
        return flop_tree_response_ranges_effective

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
