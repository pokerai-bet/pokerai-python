from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.turn_projected_range_response_200_type_1_spot_status import TurnProjectedRangeResponse200Type1SpotStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="TurnProjectedRangeResponse200Type1")



@_attrs_define
class TurnProjectedRangeResponse200Type1:
    """ 
        Attributes:
            spot_status (TurnProjectedRangeResponse200Type1SpotStatus | Unset):
     """

    spot_status: TurnProjectedRangeResponse200Type1SpotStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        spot_status: str | Unset = UNSET
        if not isinstance(self.spot_status, Unset):
            spot_status = self.spot_status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spot_status is not UNSET:
            field_dict["spot_status"] = spot_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _spot_status = d.pop("spot_status", UNSET)
        spot_status: TurnProjectedRangeResponse200Type1SpotStatus | Unset
        if isinstance(_spot_status,  Unset):
            spot_status = UNSET
        else:
            spot_status = TurnProjectedRangeResponse200Type1SpotStatus(_spot_status)




        turn_projected_range_response_200_type_1 = cls(
            spot_status=spot_status,
        )


        turn_projected_range_response_200_type_1.additional_properties = d
        return turn_projected_range_response_200_type_1

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
