from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolverScheduleRequestRaiseSizes")


@_attrs_define
class SolverScheduleRequestRaiseSizes:
    """optional per-street raise sizes in pot %; omitted streets reuse bet_sizes/defaults

    Attributes:
        flop (Union[Unset, list[int]]):
        turn (Union[Unset, list[int]]):
        river (Union[Unset, list[int]]):
    """

    flop: Union[Unset, list[int]] = UNSET
    turn: Union[Unset, list[int]] = UNSET
    river: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flop: Union[Unset, list[int]] = UNSET
        if not isinstance(self.flop, Unset):
            flop = self.flop

        turn: Union[Unset, list[int]] = UNSET
        if not isinstance(self.turn, Unset):
            turn = self.turn

        river: Union[Unset, list[int]] = UNSET
        if not isinstance(self.river, Unset):
            river = self.river

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flop is not UNSET:
            field_dict["flop"] = flop
        if turn is not UNSET:
            field_dict["turn"] = turn
        if river is not UNSET:
            field_dict["river"] = river

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flop = cast(list[int], d.pop("flop", UNSET))

        turn = cast(list[int], d.pop("turn", UNSET))

        river = cast(list[int], d.pop("river", UNSET))

        solver_schedule_request_raise_sizes = cls(
            flop=flop,
            turn=turn,
            river=river,
        )

        solver_schedule_request_raise_sizes.additional_properties = d
        return solver_schedule_request_raise_sizes

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
