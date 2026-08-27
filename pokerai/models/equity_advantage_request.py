from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EquityAdvantageRequest")


@_attrs_define
class EquityAdvantageRequest:
    """
    Attributes:
        hero (list[str]):
        villain (list[str]):
        board (str):
        sample_count (Union[None, Unset, int]):
        seed (Union[None, Unset, int]):
        hand_type (Union[None, Unset, str]):
    """

    hero: list[str]
    villain: list[str]
    board: str
    sample_count: Union[None, Unset, int] = UNSET
    seed: Union[None, Unset, int] = UNSET
    hand_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero = self.hero

        villain = self.villain

        board = self.board

        sample_count: Union[None, Unset, int]
        if isinstance(self.sample_count, Unset):
            sample_count = UNSET
        else:
            sample_count = self.sample_count

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        hand_type: Union[None, Unset, str]
        if isinstance(self.hand_type, Unset):
            hand_type = UNSET
        else:
            hand_type = self.hand_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hero": hero,
                "villain": villain,
                "board": board,
            }
        )
        if sample_count is not UNSET:
            field_dict["sample_count"] = sample_count
        if seed is not UNSET:
            field_dict["seed"] = seed
        if hand_type is not UNSET:
            field_dict["hand_type"] = hand_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hero = cast(list[str], d.pop("hero"))

        villain = cast(list[str], d.pop("villain"))

        board = d.pop("board")

        def _parse_sample_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sample_count = _parse_sample_count(d.pop("sample_count", UNSET))

        def _parse_seed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_hand_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hand_type = _parse_hand_type(d.pop("hand_type", UNSET))

        equity_advantage_request = cls(
            hero=hero,
            villain=villain,
            board=board,
            sample_count=sample_count,
            seed=seed,
            hand_type=hand_type,
        )

        equity_advantage_request.additional_properties = d
        return equity_advantage_request

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
