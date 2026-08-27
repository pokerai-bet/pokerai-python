from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preflop_range_response_200_flop_pruning_guarantees import PreflopRangeResponse200FlopPruningGuarantees
    from ..models.preflop_range_response_200_quota import PreflopRangeResponse200Quota
    from ..models.preflop_range_response_200_range import PreflopRangeResponse200Range


T = TypeVar("T", bound="PreflopRangeResponse200")


@_attrs_define
class PreflopRangeResponse200:
    """
    Attributes:
        range_ (Union[Unset, PreflopRangeResponse200Range]): hand type (AA / AKs / AKo) -> {fold, call, raise}; 169
            entries, each summing to ~1
        flop_pruning_guarantees (Union[Unset, PreflopRangeResponse200FlopPruningGuarantees]): Present only when
            include_flop_pruning_guarantees was requested. Missing data must not be used to infer a removal list.
        quota (Union[Unset, PreflopRangeResponse200Quota]):
    """

    range_: Union[Unset, "PreflopRangeResponse200Range"] = UNSET
    flop_pruning_guarantees: Union[Unset, "PreflopRangeResponse200FlopPruningGuarantees"] = UNSET
    quota: Union[Unset, "PreflopRangeResponse200Quota"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        flop_pruning_guarantees: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.flop_pruning_guarantees, Unset):
            flop_pruning_guarantees = self.flop_pruning_guarantees.to_dict()

        quota: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_
        if flop_pruning_guarantees is not UNSET:
            field_dict["flop_pruning_guarantees"] = flop_pruning_guarantees
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_response_200_flop_pruning_guarantees import (
            PreflopRangeResponse200FlopPruningGuarantees,
        )
        from ..models.preflop_range_response_200_quota import PreflopRangeResponse200Quota
        from ..models.preflop_range_response_200_range import PreflopRangeResponse200Range

        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, PreflopRangeResponse200Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = PreflopRangeResponse200Range.from_dict(_range_)

        _flop_pruning_guarantees = d.pop("flop_pruning_guarantees", UNSET)
        flop_pruning_guarantees: Union[Unset, PreflopRangeResponse200FlopPruningGuarantees]
        if isinstance(_flop_pruning_guarantees, Unset):
            flop_pruning_guarantees = UNSET
        else:
            flop_pruning_guarantees = PreflopRangeResponse200FlopPruningGuarantees.from_dict(_flop_pruning_guarantees)

        _quota = d.pop("quota", UNSET)
        quota: Union[Unset, PreflopRangeResponse200Quota]
        if isinstance(_quota, Unset):
            quota = UNSET
        else:
            quota = PreflopRangeResponse200Quota.from_dict(_quota)

        preflop_range_response_200 = cls(
            range_=range_,
            flop_pruning_guarantees=flop_pruning_guarantees,
            quota=quota,
        )

        preflop_range_response_200.additional_properties = d
        return preflop_range_response_200

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
