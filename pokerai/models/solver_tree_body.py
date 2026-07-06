from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SolverTreeBody")



@_attrs_define
class SolverTreeBody:
    """ 
        Attributes:
            solve (str): handle from /v1/gto/solver
            turn_card (str | Unset): optional; for a flop solve, the dealt turn card (e.g. "Td") — returns nodes under that
                turn.
            river_card (str | Unset): optional; the dealt river card (e.g. "Qh"). From a flop solve, pair with turn_card to
                disambiguate.
     """

    solve: str
    turn_card: str | Unset = UNSET
    river_card: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        solve = self.solve

        turn_card = self.turn_card

        river_card = self.river_card


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "solve": solve,
        })
        if turn_card is not UNSET:
            field_dict["turn_card"] = turn_card
        if river_card is not UNSET:
            field_dict["river_card"] = river_card

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        solve = d.pop("solve")

        turn_card = d.pop("turn_card", UNSET)

        river_card = d.pop("river_card", UNSET)

        solver_tree_body = cls(
            solve=solve,
            turn_card=turn_card,
            river_card=river_card,
        )


        solver_tree_body.additional_properties = d
        return solver_tree_body

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
