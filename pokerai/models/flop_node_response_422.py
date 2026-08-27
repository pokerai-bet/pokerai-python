from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flop_node_response_422_error import FlopNodeResponse422Error

T = TypeVar("T", bound="FlopNodeResponse422")


@_attrs_define
class FlopNodeResponse422:
    """
    Attributes:
        error (FlopNodeResponse422Error):
        message (str):
    """

    error: FlopNodeResponse422Error
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = FlopNodeResponse422Error(d.pop("error"))

        message = d.pop("message")

        flop_node_response_422 = cls(
            error=error,
            message=message,
        )

        flop_node_response_422.additional_properties = d
        return flop_node_response_422

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
