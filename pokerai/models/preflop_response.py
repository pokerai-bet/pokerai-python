from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preflop_response_situation import PreflopResponseSituation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota import Quota
    from ..models.strategy_item import StrategyItem


T = TypeVar("T", bound="PreflopResponse")


@_attrs_define
class PreflopResponse:
    """
    Attributes:
        hole_cards (Union[Unset, str]):
        situation (Union[Unset, PreflopResponseSituation]): table state hero faces: RFI (folded to hero, open spot) /
            Limp (a limper is in, no raise) / Raise (1 raise) / 3-Bet / 4-Bet / 5-Bet
        strategy (Union[Unset, list['StrategyItem']]):
        quota (Union[Unset, Quota]):
    """

    hole_cards: Union[Unset, str] = UNSET
    situation: Union[Unset, PreflopResponseSituation] = UNSET
    strategy: Union[Unset, list["StrategyItem"]] = UNSET
    quota: Union[Unset, "Quota"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hole_cards = self.hole_cards

        situation: Union[Unset, str] = UNSET
        if not isinstance(self.situation, Unset):
            situation = self.situation.value

        strategy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = []
            for strategy_item_data in self.strategy:
                strategy_item = strategy_item_data.to_dict()
                strategy.append(strategy_item)

        quota: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hole_cards is not UNSET:
            field_dict["hole_cards"] = hole_cards
        if situation is not UNSET:
            field_dict["situation"] = situation
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota import Quota
        from ..models.strategy_item import StrategyItem

        d = dict(src_dict)
        hole_cards = d.pop("hole_cards", UNSET)

        _situation = d.pop("situation", UNSET)
        situation: Union[Unset, PreflopResponseSituation]
        if isinstance(_situation, Unset):
            situation = UNSET
        else:
            situation = PreflopResponseSituation(_situation)

        strategy = []
        _strategy = d.pop("strategy", UNSET)
        for strategy_item_data in _strategy or []:
            strategy_item = StrategyItem.from_dict(strategy_item_data)

            strategy.append(strategy_item)

        _quota = d.pop("quota", UNSET)
        quota: Union[Unset, Quota]
        if isinstance(_quota, Unset):
            quota = UNSET
        else:
            quota = Quota.from_dict(_quota)

        preflop_response = cls(
            hole_cards=hole_cards,
            situation=situation,
            strategy=strategy,
            quota=quota,
        )

        preflop_response.additional_properties = d
        return preflop_response

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
