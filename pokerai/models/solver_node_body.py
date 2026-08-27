from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolverNodeBody")


@_attrs_define
class SolverNodeBody:
    """
    Attributes:
        node (str): node token from /v1/gto/solver/tree
        hole_cards (Union[Unset, str]): two cards, no separator, e.g. "AdKd". Rank AKQJT98765432, suit c d h s. Example:
            AdKd.
    """

    node: str
    hole_cards: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node

        hole_cards = self.hole_cards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
            }
        )
        if hole_cards is not UNSET:
            field_dict["hole_cards"] = hole_cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node = d.pop("node")

        hole_cards = d.pop("hole_cards", UNSET)

        solver_node_body = cls(
            node=node,
            hole_cards=hole_cards,
        )

        solver_node_body.additional_properties = d
        return solver_node_body

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
