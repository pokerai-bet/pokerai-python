from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.solver_tree_response_spot_status import SolverTreeResponseSpotStatus
from ..models.solver_tree_response_street import SolverTreeResponseStreet
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.solver_tree_response_nodes_item import SolverTreeResponseNodesItem





T = TypeVar("T", bound="SolverTreeResponse")



@_attrs_define
class SolverTreeResponse:
    """ 
        Attributes:
            street (SolverTreeResponseStreet | Unset):
            pot (float | Unset):
            effective_stack (float | Unset):
            spot_status (SolverTreeResponseSpotStatus | Unset): no_nodes = solve converged but the queried round/runout has
                no decision nodes in the tree (terminal — stop polling).
            node_count (int | Unset):
            nodes (list[SolverTreeResponseNodesItem] | Unset):
     """

    street: SolverTreeResponseStreet | Unset = UNSET
    pot: float | Unset = UNSET
    effective_stack: float | Unset = UNSET
    spot_status: SolverTreeResponseSpotStatus | Unset = UNSET
    node_count: int | Unset = UNSET
    nodes: list[SolverTreeResponseNodesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.solver_tree_response_nodes_item import SolverTreeResponseNodesItem
        street: str | Unset = UNSET
        if not isinstance(self.street, Unset):
            street = self.street.value


        pot = self.pot

        effective_stack = self.effective_stack

        spot_status: str | Unset = UNSET
        if not isinstance(self.spot_status, Unset):
            spot_status = self.spot_status.value


        node_count = self.node_count

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if street is not UNSET:
            field_dict["street"] = street
        if pot is not UNSET:
            field_dict["pot"] = pot
        if effective_stack is not UNSET:
            field_dict["effective_stack"] = effective_stack
        if spot_status is not UNSET:
            field_dict["spot_status"] = spot_status
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.solver_tree_response_nodes_item import SolverTreeResponseNodesItem
        d = dict(src_dict)
        _street = d.pop("street", UNSET)
        street: SolverTreeResponseStreet | Unset
        if isinstance(_street,  Unset):
            street = UNSET
        else:
            street = SolverTreeResponseStreet(_street)




        pot = d.pop("pot", UNSET)

        effective_stack = d.pop("effective_stack", UNSET)

        _spot_status = d.pop("spot_status", UNSET)
        spot_status: SolverTreeResponseSpotStatus | Unset
        if isinstance(_spot_status,  Unset):
            spot_status = UNSET
        else:
            spot_status = SolverTreeResponseSpotStatus(_spot_status)




        node_count = d.pop("node_count", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[SolverTreeResponseNodesItem] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = SolverTreeResponseNodesItem.from_dict(nodes_item_data)



                nodes.append(nodes_item)


        solver_tree_response = cls(
            street=street,
            pot=pot,
            effective_stack=effective_stack,
            spot_status=spot_status,
            node_count=node_count,
            nodes=nodes,
        )


        solver_tree_response.additional_properties = d
        return solver_tree_response

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
