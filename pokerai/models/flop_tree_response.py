from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.flop_tree_response_nodes_item import FlopTreeResponseNodesItem
  from ..models.quota import Quota





T = TypeVar("T", bound="FlopTreeResponse")



@_attrs_define
class FlopTreeResponse:
    """ 
        Attributes:
            board (list[str] | Unset): community cards returned as an array Example: ['2c', '2h', '2s'].
            pot_type (str | Unset):
            pot (float | Unset):
            effective_stack (float | Unset):
            oop_range (str | Unset): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1,
                default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
            ip_range (str | Unset): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1,
                default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
            node_count (int | Unset):
            nodes (list[FlopTreeResponseNodesItem] | Unset):
            quota (Quota | Unset):
     """

    board: list[str] | Unset = UNSET
    pot_type: str | Unset = UNSET
    pot: float | Unset = UNSET
    effective_stack: float | Unset = UNSET
    oop_range: str | Unset = UNSET
    ip_range: str | Unset = UNSET
    node_count: int | Unset = UNSET
    nodes: list[FlopTreeResponseNodesItem] | Unset = UNSET
    quota: Quota | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.flop_tree_response_nodes_item import FlopTreeResponseNodesItem
        from ..models.quota import Quota
        board: list[str] | Unset = UNSET
        if not isinstance(self.board, Unset):
            board = self.board



        pot_type = self.pot_type

        pot = self.pot

        effective_stack = self.effective_stack

        oop_range = self.oop_range

        ip_range = self.ip_range

        node_count = self.node_count

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)



        quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if board is not UNSET:
            field_dict["board"] = board
        if pot_type is not UNSET:
            field_dict["pot_type"] = pot_type
        if pot is not UNSET:
            field_dict["pot"] = pot
        if effective_stack is not UNSET:
            field_dict["effective_stack"] = effective_stack
        if oop_range is not UNSET:
            field_dict["oop_range"] = oop_range
        if ip_range is not UNSET:
            field_dict["ip_range"] = ip_range
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flop_tree_response_nodes_item import FlopTreeResponseNodesItem
        from ..models.quota import Quota
        d = dict(src_dict)
        board = cast(list[str], d.pop("board", UNSET))


        pot_type = d.pop("pot_type", UNSET)

        pot = d.pop("pot", UNSET)

        effective_stack = d.pop("effective_stack", UNSET)

        oop_range = d.pop("oop_range", UNSET)

        ip_range = d.pop("ip_range", UNSET)

        node_count = d.pop("node_count", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[FlopTreeResponseNodesItem] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = FlopTreeResponseNodesItem.from_dict(nodes_item_data)



                nodes.append(nodes_item)


        _quota = d.pop("quota", UNSET)
        quota: Quota | Unset
        if isinstance(_quota,  Unset):
            quota = UNSET
        else:
            quota = Quota.from_dict(_quota)




        flop_tree_response = cls(
            board=board,
            pot_type=pot_type,
            pot=pot,
            effective_stack=effective_stack,
            oop_range=oop_range,
            ip_range=ip_range,
            node_count=node_count,
            nodes=nodes,
            quota=quota,
        )


        flop_tree_response.additional_properties = d
        return flop_tree_response

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
