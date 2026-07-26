from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StrategyItem")


@_attrs_define
class StrategyItem:
    """
    Attributes:
        action (str): check / call / fold / raise / bet
        frequency (float): 0..1 probability
        sizing_pot (Union[Unset, float]): pot-relative sizing, standard % pot convention: a bet = bet ÷ pot; a raise =
            (raise − amount-to-call) ÷ pot-after-call. e.g. 0.5 / 0.8 / 1. bet/raise only
        amount_bb (Union[Unset, float]): absolute bet/raise amount in BB (for bet/raise)
        allin (Union[Unset, bool]): present and true when the action is all-in
    """

    action: str
    frequency: float
    sizing_pot: Union[Unset, float] = UNSET
    amount_bb: Union[Unset, float] = UNSET
    allin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        frequency = self.frequency

        sizing_pot = self.sizing_pot

        amount_bb = self.amount_bb

        allin = self.allin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "frequency": frequency,
            }
        )
        if sizing_pot is not UNSET:
            field_dict["sizing_pot"] = sizing_pot
        if amount_bb is not UNSET:
            field_dict["amount_bb"] = amount_bb
        if allin is not UNSET:
            field_dict["allin"] = allin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        frequency = d.pop("frequency")

        sizing_pot = d.pop("sizing_pot", UNSET)

        amount_bb = d.pop("amount_bb", UNSET)

        allin = d.pop("allin", UNSET)

        strategy_item = cls(
            action=action,
            frequency=frequency,
            sizing_pot=sizing_pot,
            amount_bb=amount_bb,
            allin=allin,
        )

        strategy_item.additional_properties = d
        return strategy_item

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
