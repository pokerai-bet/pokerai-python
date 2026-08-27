from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HandStrengthRequest")


@_attrs_define
class HandStrengthRequest:
    """
    Attributes:
        hole_range (list[str]): hero range/hand (notation)
        board (Union[Unset, str]):  Default: ''.
        player_count (Union[Unset, int]):  Default: 2.
        sample_count (Union[None, Unset, int]):
        seed (Union[None, Unset, int]):
    """

    hole_range: list[str]
    board: Union[Unset, str] = ""
    player_count: Union[Unset, int] = 2
    sample_count: Union[None, Unset, int] = UNSET
    seed: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hole_range = self.hole_range

        board = self.board

        player_count = self.player_count

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hole_range": hole_range,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if player_count is not UNSET:
            field_dict["player_count"] = player_count
        if sample_count is not UNSET:
            field_dict["sample_count"] = sample_count
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hole_range = cast(list[str], d.pop("hole_range"))

        board = d.pop("board", UNSET)

        player_count = d.pop("player_count", UNSET)

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

        hand_strength_request = cls(
            hole_range=hole_range,
            board=board,
            player_count=player_count,
            sample_count=sample_count,
            seed=seed,
        )

        hand_strength_request.additional_properties = d
        return hand_strength_request

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
