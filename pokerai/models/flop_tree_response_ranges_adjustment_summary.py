from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopTreeResponseRangesAdjustmentSummary")


@_attrs_define
class FlopTreeResponseRangesAdjustmentSummary:
    """
    Attributes:
        oop_removed (Union[Unset, float]):
        oop_reweighted (Union[Unset, float]):
        ip_removed (Union[Unset, float]):
        ip_reweighted (Union[Unset, float]):
    """

    oop_removed: Union[Unset, float] = UNSET
    oop_reweighted: Union[Unset, float] = UNSET
    ip_removed: Union[Unset, float] = UNSET
    ip_reweighted: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oop_removed = self.oop_removed

        oop_reweighted = self.oop_reweighted

        ip_removed = self.ip_removed

        ip_reweighted = self.ip_reweighted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oop_removed is not UNSET:
            field_dict["oop_removed"] = oop_removed
        if oop_reweighted is not UNSET:
            field_dict["oop_reweighted"] = oop_reweighted
        if ip_removed is not UNSET:
            field_dict["ip_removed"] = ip_removed
        if ip_reweighted is not UNSET:
            field_dict["ip_reweighted"] = ip_reweighted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oop_removed = d.pop("oop_removed", UNSET)

        oop_reweighted = d.pop("oop_reweighted", UNSET)

        ip_removed = d.pop("ip_removed", UNSET)

        ip_reweighted = d.pop("ip_reweighted", UNSET)

        flop_tree_response_ranges_adjustment_summary = cls(
            oop_removed=oop_removed,
            oop_reweighted=oop_reweighted,
            ip_removed=ip_removed,
            ip_reweighted=ip_reweighted,
        )

        flop_tree_response_ranges_adjustment_summary.additional_properties = d
        return flop_tree_response_ranges_adjustment_summary

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
