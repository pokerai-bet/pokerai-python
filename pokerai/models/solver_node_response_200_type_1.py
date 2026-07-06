from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.solver_node_response_200_type_1_node_status import SolverNodeResponse200Type1NodeStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="SolverNodeResponse200Type1")



@_attrs_define
class SolverNodeResponse200Type1:
    """ 
        Attributes:
            node_status (SolverNodeResponse200Type1NodeStatus | Unset): expired = solve reclaimed/replaced, reschedule;
                error = solver per-node strategy_error (with message); computing = still solving.
            message (str | Unset): present on node_status = error
     """

    node_status: SolverNodeResponse200Type1NodeStatus | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        node_status: str | Unset = UNSET
        if not isinstance(self.node_status, Unset):
            node_status = self.node_status.value


        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if node_status is not UNSET:
            field_dict["node_status"] = node_status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _node_status = d.pop("node_status", UNSET)
        node_status: SolverNodeResponse200Type1NodeStatus | Unset
        if isinstance(_node_status,  Unset):
            node_status = UNSET
        else:
            node_status = SolverNodeResponse200Type1NodeStatus(_node_status)




        message = d.pop("message", UNSET)

        solver_node_response_200_type_1 = cls(
            node_status=node_status,
            message=message,
        )


        solver_node_response_200_type_1.additional_properties = d
        return solver_node_response_200_type_1

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
