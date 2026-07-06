from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.evs_response_evs import EvsResponseEvs





T = TypeVar("T", bound="EvsResponse")



@_attrs_define
class EvsResponse:
    """ Per-hand, per-action EVs at the node; each hand's EV array aligns with actions.

        Attributes:
            node_id (str | Unset):
            task_id (str | Unset):
            player (int | Unset):
            round_ (str | Unset):  Example: FLOP.
            actions (list[str] | Unset):  Example: ['CHECK', 'BET 4.000000', 'BET 97.000000'].
            evs (EvsResponseEvs | Unset): hand -> per-action EV array (bb); a single array when hand is given Example:
                {'2c2d': [-0.826359, -0.792223, -1.643411]}.
     """

    node_id: str | Unset = UNSET
    task_id: str | Unset = UNSET
    player: int | Unset = UNSET
    round_: str | Unset = UNSET
    actions: list[str] | Unset = UNSET
    evs: EvsResponseEvs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.evs_response_evs import EvsResponseEvs
        node_id = self.node_id

        task_id = self.task_id

        player = self.player

        round_ = self.round_

        actions: list[str] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions



        evs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evs, Unset):
            evs = self.evs.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if player is not UNSET:
            field_dict["player"] = player
        if round_ is not UNSET:
            field_dict["round"] = round_
        if actions is not UNSET:
            field_dict["actions"] = actions
        if evs is not UNSET:
            field_dict["evs"] = evs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evs_response_evs import EvsResponseEvs
        d = dict(src_dict)
        node_id = d.pop("node_id", UNSET)

        task_id = d.pop("task_id", UNSET)

        player = d.pop("player", UNSET)

        round_ = d.pop("round", UNSET)

        actions = cast(list[str], d.pop("actions", UNSET))


        _evs = d.pop("evs", UNSET)
        evs: EvsResponseEvs | Unset
        if isinstance(_evs,  Unset):
            evs = UNSET
        else:
            evs = EvsResponseEvs.from_dict(_evs)




        evs_response = cls(
            node_id=node_id,
            task_id=task_id,
            player=player,
            round_=round_,
            actions=actions,
            evs=evs,
        )


        evs_response.additional_properties = d
        return evs_response

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
