from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EvsRequest")



@_attrs_define
class EvsRequest:
    """ 
        Attributes:
            solve (str): handle from /v1/gto/solver
            node_id (str): a node from /v1/gto/solver/tree (solver notation, e.g. "root/CHECK/BET 6.000000") Example: root.
            hand (str | Unset): optional; filter to one hand's EVs (else all hands) Example: AsKh.
     """

    solve: str
    node_id: str
    hand: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        solve = self.solve

        node_id = self.node_id

        hand = self.hand


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "solve": solve,
            "node_id": node_id,
        })
        if hand is not UNSET:
            field_dict["hand"] = hand

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        solve = d.pop("solve")

        node_id = d.pop("node_id")

        hand = d.pop("hand", UNSET)

        evs_request = cls(
            solve=solve,
            node_id=node_id,
            hand=hand,
        )


        evs_request.additional_properties = d
        return evs_request

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
