from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeStrategyResponseActionsItem")


@_attrs_define
class NodeStrategyResponseActionsItem:
    """
    Attributes:
        action (Union[Unset, str]):
        amount_bb (Union[Unset, float]):
        sizing_pot (Union[Unset, float]):
        allin (Union[Unset, bool]):
    """

    action: Union[Unset, str] = UNSET
    amount_bb: Union[Unset, float] = UNSET
    sizing_pot: Union[Unset, float] = UNSET
    allin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        amount_bb = self.amount_bb

        sizing_pot = self.sizing_pot

        allin = self.allin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if amount_bb is not UNSET:
            field_dict["amount_bb"] = amount_bb
        if sizing_pot is not UNSET:
            field_dict["sizing_pot"] = sizing_pot
        if allin is not UNSET:
            field_dict["allin"] = allin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        amount_bb = d.pop("amount_bb", UNSET)

        sizing_pot = d.pop("sizing_pot", UNSET)

        allin = d.pop("allin", UNSET)

        node_strategy_response_actions_item = cls(
            action=action,
            amount_bb=amount_bb,
            sizing_pot=sizing_pot,
            allin=allin,
        )

        node_strategy_response_actions_item.additional_properties = d
        return node_strategy_response_actions_item

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
