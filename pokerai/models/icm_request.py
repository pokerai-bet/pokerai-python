from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IcmRequest")


@_attrs_define
class IcmRequest:
    """
    Attributes:
        payouts (list[float]):
        chips (list[float]):
    """

    payouts: list[float]
    chips: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payouts = self.payouts

        chips = self.chips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payouts": payouts,
                "chips": chips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payouts = cast(list[float], d.pop("payouts"))

        chips = cast(list[float], d.pop("chips"))

        icm_request = cls(
            payouts=payouts,
            chips=chips,
        )

        icm_request.additional_properties = d
        return icm_request

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
