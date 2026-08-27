from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopTreeResponseNodesItem")


@_attrs_define
class FlopTreeResponseNodesItem:
    """
    Attributes:
        node (Union[Unset, str]):  Example: root/CHECK/BET_8.
        is_hero (Union[Unset, bool]):
        token (Union[Unset, str]):
    """

    node: Union[Unset, str] = UNSET
    is_hero: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node

        is_hero = self.is_hero

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node
        if is_hero is not UNSET:
            field_dict["is_hero"] = is_hero
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node = d.pop("node", UNSET)

        is_hero = d.pop("is_hero", UNSET)

        token = d.pop("token", UNSET)

        flop_tree_response_nodes_item = cls(
            node=node,
            is_hero=is_hero,
            token=token,
        )

        flop_tree_response_nodes_item.additional_properties = d
        return flop_tree_response_nodes_item

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
