from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flop_tree_response_ranges_adjustment_summary import FlopTreeResponseRangesAdjustmentSummary
    from ..models.flop_tree_response_ranges_effective import FlopTreeResponseRangesEffective
    from ..models.flop_tree_response_ranges_requested import FlopTreeResponseRangesRequested


T = TypeVar("T", bound="FlopTreeResponseRanges")


@_attrs_define
class FlopTreeResponseRanges:
    """Requested and effective starting ranges. Effective is the strategy-tree source; adjusted states whether they differ.

    Attributes:
        requested (Union[Unset, FlopTreeResponseRangesRequested]):
        effective (Union[Unset, FlopTreeResponseRangesEffective]):
        adjusted (Union[Unset, bool]):
        adjustment_summary (Union[Unset, FlopTreeResponseRangesAdjustmentSummary]):
    """

    requested: Union[Unset, "FlopTreeResponseRangesRequested"] = UNSET
    effective: Union[Unset, "FlopTreeResponseRangesEffective"] = UNSET
    adjusted: Union[Unset, bool] = UNSET
    adjustment_summary: Union[Unset, "FlopTreeResponseRangesAdjustmentSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.requested, Unset):
            requested = self.requested.to_dict()

        effective: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective, Unset):
            effective = self.effective.to_dict()

        adjusted = self.adjusted

        adjustment_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.adjustment_summary, Unset):
            adjustment_summary = self.adjustment_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested is not UNSET:
            field_dict["requested"] = requested
        if effective is not UNSET:
            field_dict["effective"] = effective
        if adjusted is not UNSET:
            field_dict["adjusted"] = adjusted
        if adjustment_summary is not UNSET:
            field_dict["adjustment_summary"] = adjustment_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flop_tree_response_ranges_adjustment_summary import FlopTreeResponseRangesAdjustmentSummary
        from ..models.flop_tree_response_ranges_effective import FlopTreeResponseRangesEffective
        from ..models.flop_tree_response_ranges_requested import FlopTreeResponseRangesRequested

        d = dict(src_dict)
        _requested = d.pop("requested", UNSET)
        requested: Union[Unset, FlopTreeResponseRangesRequested]
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = FlopTreeResponseRangesRequested.from_dict(_requested)

        _effective = d.pop("effective", UNSET)
        effective: Union[Unset, FlopTreeResponseRangesEffective]
        if isinstance(_effective, Unset):
            effective = UNSET
        else:
            effective = FlopTreeResponseRangesEffective.from_dict(_effective)

        adjusted = d.pop("adjusted", UNSET)

        _adjustment_summary = d.pop("adjustment_summary", UNSET)
        adjustment_summary: Union[Unset, FlopTreeResponseRangesAdjustmentSummary]
        if isinstance(_adjustment_summary, Unset):
            adjustment_summary = UNSET
        else:
            adjustment_summary = FlopTreeResponseRangesAdjustmentSummary.from_dict(_adjustment_summary)

        flop_tree_response_ranges = cls(
            requested=requested,
            effective=effective,
            adjusted=adjusted,
            adjustment_summary=adjustment_summary,
        )

        flop_tree_response_ranges.additional_properties = d
        return flop_tree_response_ranges

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
