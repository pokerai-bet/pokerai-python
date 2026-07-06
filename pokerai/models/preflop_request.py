from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.preflop_request_preflop_version import PreflopRequestPreflopVersion
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.preflop_request_positions import PreflopRequestPositions
  from ..models.preflop_request_preflop_actions_item import PreflopRequestPreflopActionsItem





T = TypeVar("T", bound="PreflopRequest")



@_attrs_define
class PreflopRequest:
    """ 
        Attributes:
            hole_cards (str): two cards, no separator, e.g. "AdKd". Rank AKQJT98765432, suit c d h s. Example: AdKd.
            positions (PreflopRequestPositions):
            preflop_actions (list[PreflopRequestPreflopActionsItem]): Explicit, complete action sequence from the small
                blind up to the player right before hero (hero is NOT included; hero's position is positions.hero). Must start
                with small blind (0.5) then big blind (1). amount is the increment newly committed this action in BB (not the
                running total); pot = sum of all amounts. A raise's resulting total must exceed the current bet and meet the
                min-raise (= current bet + size of the last raise) unless allin:true; a call's total must exactly match the
                current bet unless allin:true. Exact amounts only make the pot/sizing_pot exact — GTO frequencies are situation-
                based (RFI/3bet/4bet + positions) and do not change with bet sizes. Violations return 400 invalid_actions.
            table_size (str | Unset):  Default: '6max'.
            preflop_version (PreflopRequestPreflopVersion | Unset): optional; which 6max preflop chart set to use. Omit for
                the platform default (6max). Unknown value -> 400 unsupported_preflop_version.
     """

    hole_cards: str
    positions: PreflopRequestPositions
    preflop_actions: list[PreflopRequestPreflopActionsItem]
    table_size: str | Unset = '6max'
    preflop_version: PreflopRequestPreflopVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.preflop_request_positions import PreflopRequestPositions
        from ..models.preflop_request_preflop_actions_item import PreflopRequestPreflopActionsItem
        hole_cards = self.hole_cards

        positions = self.positions.to_dict()

        preflop_actions = []
        for preflop_actions_item_data in self.preflop_actions:
            preflop_actions_item = preflop_actions_item_data.to_dict()
            preflop_actions.append(preflop_actions_item)



        table_size = self.table_size

        preflop_version: str | Unset = UNSET
        if not isinstance(self.preflop_version, Unset):
            preflop_version = self.preflop_version.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hole_cards": hole_cards,
            "positions": positions,
            "preflop_actions": preflop_actions,
        })
        if table_size is not UNSET:
            field_dict["table_size"] = table_size
        if preflop_version is not UNSET:
            field_dict["preflop_version"] = preflop_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_request_positions import PreflopRequestPositions
        from ..models.preflop_request_preflop_actions_item import PreflopRequestPreflopActionsItem
        d = dict(src_dict)
        hole_cards = d.pop("hole_cards")

        positions = PreflopRequestPositions.from_dict(d.pop("positions"))




        preflop_actions = []
        _preflop_actions = d.pop("preflop_actions")
        for preflop_actions_item_data in (_preflop_actions):
            preflop_actions_item = PreflopRequestPreflopActionsItem.from_dict(preflop_actions_item_data)



            preflop_actions.append(preflop_actions_item)


        table_size = d.pop("table_size", UNSET)

        _preflop_version = d.pop("preflop_version", UNSET)
        preflop_version: PreflopRequestPreflopVersion | Unset
        if isinstance(_preflop_version,  Unset):
            preflop_version = UNSET
        else:
            preflop_version = PreflopRequestPreflopVersion(_preflop_version)




        preflop_request = cls(
            hole_cards=hole_cards,
            positions=positions,
            preflop_actions=preflop_actions,
            table_size=table_size,
            preflop_version=preflop_version,
        )


        preflop_request.additional_properties = d
        return preflop_request

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
