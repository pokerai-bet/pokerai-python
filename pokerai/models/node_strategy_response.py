from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.node_strategy_response_actions_item import NodeStrategyResponseActionsItem
  from ..models.node_strategy_response_range_strategy import NodeStrategyResponseRangeStrategy
  from ..models.strategy_item import StrategyItem





T = TypeVar("T", bound="NodeStrategyResponse")



@_attrs_define
class NodeStrategyResponse:
    """ hero node has `strategy`; villain node (or no hole_cards) has `actions` + `range_strategy`.

        Attributes:
            node (str | Unset):
            is_hero (bool | Unset):
            hole_cards (str | Unset):
            strategy (list[StrategyItem] | Unset):
            actions (list[NodeStrategyResponseActionsItem] | Unset):
            range_strategy (NodeStrategyResponseRangeStrategy | Unset): combo (e.g. "AhKh") -> frequencies aligned to
                actions
            range_hand_count (int | Unset):
     """

    node: str | Unset = UNSET
    is_hero: bool | Unset = UNSET
    hole_cards: str | Unset = UNSET
    strategy: list[StrategyItem] | Unset = UNSET
    actions: list[NodeStrategyResponseActionsItem] | Unset = UNSET
    range_strategy: NodeStrategyResponseRangeStrategy | Unset = UNSET
    range_hand_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.node_strategy_response_actions_item import NodeStrategyResponseActionsItem
        from ..models.node_strategy_response_range_strategy import NodeStrategyResponseRangeStrategy
        from ..models.strategy_item import StrategyItem
        node = self.node

        is_hero = self.is_hero

        hole_cards = self.hole_cards

        strategy: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = []
            for strategy_item_data in self.strategy:
                strategy_item = strategy_item_data.to_dict()
                strategy.append(strategy_item)



        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)



        range_strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_strategy, Unset):
            range_strategy = self.range_strategy.to_dict()

        range_hand_count = self.range_hand_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if node is not UNSET:
            field_dict["node"] = node
        if is_hero is not UNSET:
            field_dict["is_hero"] = is_hero
        if hole_cards is not UNSET:
            field_dict["hole_cards"] = hole_cards
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if actions is not UNSET:
            field_dict["actions"] = actions
        if range_strategy is not UNSET:
            field_dict["range_strategy"] = range_strategy
        if range_hand_count is not UNSET:
            field_dict["range_hand_count"] = range_hand_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_strategy_response_actions_item import NodeStrategyResponseActionsItem
        from ..models.node_strategy_response_range_strategy import NodeStrategyResponseRangeStrategy
        from ..models.strategy_item import StrategyItem
        d = dict(src_dict)
        node = d.pop("node", UNSET)

        is_hero = d.pop("is_hero", UNSET)

        hole_cards = d.pop("hole_cards", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: list[StrategyItem] | Unset = UNSET
        if _strategy is not UNSET:
            strategy = []
            for strategy_item_data in _strategy:
                strategy_item = StrategyItem.from_dict(strategy_item_data)



                strategy.append(strategy_item)


        _actions = d.pop("actions", UNSET)
        actions: list[NodeStrategyResponseActionsItem] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = NodeStrategyResponseActionsItem.from_dict(actions_item_data)



                actions.append(actions_item)


        _range_strategy = d.pop("range_strategy", UNSET)
        range_strategy: NodeStrategyResponseRangeStrategy | Unset
        if isinstance(_range_strategy,  Unset):
            range_strategy = UNSET
        else:
            range_strategy = NodeStrategyResponseRangeStrategy.from_dict(_range_strategy)




        range_hand_count = d.pop("range_hand_count", UNSET)

        node_strategy_response = cls(
            node=node,
            is_hero=is_hero,
            hole_cards=hole_cards,
            strategy=strategy,
            actions=actions,
            range_strategy=range_strategy,
            range_hand_count=range_hand_count,
        )


        node_strategy_response.additional_properties = d
        return node_strategy_response

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
