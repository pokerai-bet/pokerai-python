from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.turn_projected_range_request_hero_position import TurnProjectedRangeRequestHeroPosition
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TurnProjectedRangeRequest")



@_attrs_define
class TurnProjectedRangeRequest:
    """ 
        Attributes:
            solve (str): handle from /v1/gto/solver (a turn solve)
            node_id (str): a turn action line; may end in the street-closing CALL/CHECK. Solver node format with spaces,
                e.g. "root/CHECK/BET 6.000000/CALL".
            normalize (bool | Unset):  Default: True.
            bluff_discount_ratio (float | Unset):
            hero_position (TurnProjectedRangeRequestHeroPosition | Unset): optional card blocking, pair with hero_hand.
            hero_hand (str | Unset): optional card blocking: remove every combo containing one of Hero's cards from the
                villain's updated range. Example: AsKs.
            partner_hands (list[str] | Unset): optional; 4-char combos whose cards are removed from the villain's updated
                range. Requires hero_position. Input only. Example: ['Ac9c'].
     """

    solve: str
    node_id: str
    normalize: bool | Unset = True
    bluff_discount_ratio: float | Unset = UNSET
    hero_position: TurnProjectedRangeRequestHeroPosition | Unset = UNSET
    hero_hand: str | Unset = UNSET
    partner_hands: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        solve = self.solve

        node_id = self.node_id

        normalize = self.normalize

        bluff_discount_ratio = self.bluff_discount_ratio

        hero_position: str | Unset = UNSET
        if not isinstance(self.hero_position, Unset):
            hero_position = self.hero_position.value


        hero_hand = self.hero_hand

        partner_hands: list[str] | Unset = UNSET
        if not isinstance(self.partner_hands, Unset):
            partner_hands = self.partner_hands




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "solve": solve,
            "node_id": node_id,
        })
        if normalize is not UNSET:
            field_dict["normalize"] = normalize
        if bluff_discount_ratio is not UNSET:
            field_dict["bluff_discount_ratio"] = bluff_discount_ratio
        if hero_position is not UNSET:
            field_dict["hero_position"] = hero_position
        if hero_hand is not UNSET:
            field_dict["hero_hand"] = hero_hand
        if partner_hands is not UNSET:
            field_dict["partner_hands"] = partner_hands

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        solve = d.pop("solve")

        node_id = d.pop("node_id")

        normalize = d.pop("normalize", UNSET)

        bluff_discount_ratio = d.pop("bluff_discount_ratio", UNSET)

        _hero_position = d.pop("hero_position", UNSET)
        hero_position: TurnProjectedRangeRequestHeroPosition | Unset
        if isinstance(_hero_position,  Unset):
            hero_position = UNSET
        else:
            hero_position = TurnProjectedRangeRequestHeroPosition(_hero_position)




        hero_hand = d.pop("hero_hand", UNSET)

        partner_hands = cast(list[str], d.pop("partner_hands", UNSET))


        turn_projected_range_request = cls(
            solve=solve,
            node_id=node_id,
            normalize=normalize,
            bluff_discount_ratio=bluff_discount_ratio,
            hero_position=hero_position,
            hero_hand=hero_hand,
            partner_hands=partner_hands,
        )


        turn_projected_range_request.additional_properties = d
        return turn_projected_range_request

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
