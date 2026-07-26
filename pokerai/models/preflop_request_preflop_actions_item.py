from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position import Position
from ..models.preflop_request_preflop_actions_item_action import PreflopRequestPreflopActionsItemAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreflopRequestPreflopActionsItem")


@_attrs_define
class PreflopRequestPreflopActionsItem:
    """
    Attributes:
        position (Position):
        action (PreflopRequestPreflopActionsItemAction):
        amount (Union[Unset, float]): increment newly committed this action in BB (required for non-fold actions);
            omitted/0 for fold
        allin (Union[Unset, bool]): optional; mark a short all-in (raise/call below the min-raise). when true, the min-
            raise check is skipped
    """

    position: Position
    action: PreflopRequestPreflopActionsItemAction
    amount: Union[Unset, float] = UNSET
    allin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position.value

        action = self.action.value

        amount = self.amount

        allin = self.allin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "action": action,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if allin is not UNSET:
            field_dict["allin"] = allin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = Position(d.pop("position"))

        action = PreflopRequestPreflopActionsItemAction(d.pop("action"))

        amount = d.pop("amount", UNSET)

        allin = d.pop("allin", UNSET)

        preflop_request_preflop_actions_item = cls(
            position=position,
            action=action,
            amount=amount,
            allin=allin,
        )

        preflop_request_preflop_actions_item.additional_properties = d
        return preflop_request_preflop_actions_item

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
