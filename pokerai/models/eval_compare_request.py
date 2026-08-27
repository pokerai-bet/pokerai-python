from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvalCompareRequest")


@_attrs_define
class EvalCompareRequest:
    """
    Attributes:
        holdings (list[str]): 2+ holdings to rank
        board (Union[Unset, str]):  Default: ''.
        hand_type (Union[None, Unset, str]):
    """

    holdings: list[str]
    board: Union[Unset, str] = ""
    hand_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holdings = self.holdings

        board = self.board

        hand_type: Union[None, Unset, str]
        if isinstance(self.hand_type, Unset):
            hand_type = UNSET
        else:
            hand_type = self.hand_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "holdings": holdings,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if hand_type is not UNSET:
            field_dict["hand_type"] = hand_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        holdings = cast(list[str], d.pop("holdings"))

        board = d.pop("board", UNSET)

        def _parse_hand_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hand_type = _parse_hand_type(d.pop("hand_type", UNSET))

        eval_compare_request = cls(
            holdings=holdings,
            board=board,
            hand_type=hand_type,
        )

        eval_compare_request.additional_properties = d
        return eval_compare_request

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
