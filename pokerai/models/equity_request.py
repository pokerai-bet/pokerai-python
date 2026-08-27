from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EquityRequest")


@_attrs_define
class EquityRequest:
    """
    Attributes:
        ranges (list[list[str]]): per-player ranges (notation)
        board (Union[Unset, str]):  Default: ''.
        sample_count (Union[None, Unset, int]): Monte-Carlo samples (capped); default applies if unset
        seed (Union[None, Unset, int]): seed for reproducible sampling
    """

    ranges: list[list[str]]
    board: Union[Unset, str] = ""
    sample_count: Union[None, Unset, int] = UNSET
    seed: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ranges = []
        for ranges_item_data in self.ranges:
            ranges_item = ranges_item_data

            ranges.append(ranges_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ranges": ranges,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if sample_count is not UNSET:
            field_dict["sample_count"] = sample_count
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ranges = []
        _ranges = d.pop("ranges")
        for ranges_item_data in _ranges:
            ranges_item = cast(list[str], ranges_item_data)

            ranges.append(ranges_item)

        board = d.pop("board", UNSET)

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

        equity_request = cls(
            ranges=ranges,
            board=board,
            sample_count=sample_count,
            seed=seed,
        )

        equity_request.additional_properties = d
        return equity_request

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
