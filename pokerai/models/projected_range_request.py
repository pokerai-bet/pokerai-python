from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.projected_range_request_flop_version import ProjectedRangeRequestFlopVersion
from ..models.projected_range_request_hero_position import ProjectedRangeRequestHeroPosition
from ..models.projected_range_request_pot_type import ProjectedRangeRequestPotType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.flop_positions import FlopPositions





T = TypeVar("T", bound="ProjectedRangeRequest")



@_attrs_define
class ProjectedRangeRequest:
    """ 
        Attributes:
            board (str): community cards as a no-separator string: 3=flop "2c2h2s", 4=turn, 5=river. Example: 2c2h2s.
            pot_type (ProjectedRangeRequestPotType):
            positions (FlopPositions): required keys depend on pot_type — SRP: hero,raiser,caller; 3BET/4BET:
                hero,raiser,three_bettor (for 4BET, raiser = the opener who 4-bet, three_bettor = the 3-bettor who called; no
                four_bettor key); LIMP: hero,limper. hero must be one of the named seats.
            node_id (str | Unset):  Default: 'root'. Example: root/BET_4.
            normalize (bool | Unset):  Default: True.
            bluff_discount_ratio (float | Unset):  Default: 0.8.
            hero_position (ProjectedRangeRequestHeroPosition | Unset): optional card blocking, pair with hero_hand.
            hero_hand (str | Unset): optional card blocking: remove every combo containing one of Hero's cards from the
                villain's updated range (the range_*_new_raw outputs). Hero's own hand is also ensured present in Hero's own
                range. Echoed back. Example: AsKs.
            bluff_combos_ratio (float | Unset): optional; fraction of the range treated as bluffs (bottom-of-range). Omit to
                use the server turn/river default. Echoed back.
            partner_hands (list[str] | Unset): optional; 4-char combos whose cards are removed from the villain's updated
                range (range_*_new_raw). Requires hero_position. Input only (not echoed). flop/projected-range only. Example:
                ['Ac9c'].
            flop_version (ProjectedRangeRequestFlopVersion | Unset): optional; which flop dataset (one solved per preflop
                version). Omit for the default (6max). If the chosen version has no data for the spot the service degrades
                gracefully to 6max. Unknown value -> 400 unsupported_flop_version. Independent of preflop_version.
     """

    board: str
    pot_type: ProjectedRangeRequestPotType
    positions: FlopPositions
    node_id: str | Unset = 'root'
    normalize: bool | Unset = True
    bluff_discount_ratio: float | Unset = 0.8
    hero_position: ProjectedRangeRequestHeroPosition | Unset = UNSET
    hero_hand: str | Unset = UNSET
    bluff_combos_ratio: float | Unset = UNSET
    partner_hands: list[str] | Unset = UNSET
    flop_version: ProjectedRangeRequestFlopVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.flop_positions import FlopPositions
        board = self.board

        pot_type = self.pot_type.value

        positions = self.positions.to_dict()

        node_id = self.node_id

        normalize = self.normalize

        bluff_discount_ratio = self.bluff_discount_ratio

        hero_position: str | Unset = UNSET
        if not isinstance(self.hero_position, Unset):
            hero_position = self.hero_position.value


        hero_hand = self.hero_hand

        bluff_combos_ratio = self.bluff_combos_ratio

        partner_hands: list[str] | Unset = UNSET
        if not isinstance(self.partner_hands, Unset):
            partner_hands = self.partner_hands



        flop_version: str | Unset = UNSET
        if not isinstance(self.flop_version, Unset):
            flop_version = self.flop_version.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "board": board,
            "pot_type": pot_type,
            "positions": positions,
        })
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if normalize is not UNSET:
            field_dict["normalize"] = normalize
        if bluff_discount_ratio is not UNSET:
            field_dict["bluff_discount_ratio"] = bluff_discount_ratio
        if hero_position is not UNSET:
            field_dict["hero_position"] = hero_position
        if hero_hand is not UNSET:
            field_dict["hero_hand"] = hero_hand
        if bluff_combos_ratio is not UNSET:
            field_dict["bluff_combos_ratio"] = bluff_combos_ratio
        if partner_hands is not UNSET:
            field_dict["partner_hands"] = partner_hands
        if flop_version is not UNSET:
            field_dict["flop_version"] = flop_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flop_positions import FlopPositions
        d = dict(src_dict)
        board = d.pop("board")

        pot_type = ProjectedRangeRequestPotType(d.pop("pot_type"))




        positions = FlopPositions.from_dict(d.pop("positions"))




        node_id = d.pop("node_id", UNSET)

        normalize = d.pop("normalize", UNSET)

        bluff_discount_ratio = d.pop("bluff_discount_ratio", UNSET)

        _hero_position = d.pop("hero_position", UNSET)
        hero_position: ProjectedRangeRequestHeroPosition | Unset
        if isinstance(_hero_position,  Unset):
            hero_position = UNSET
        else:
            hero_position = ProjectedRangeRequestHeroPosition(_hero_position)




        hero_hand = d.pop("hero_hand", UNSET)

        bluff_combos_ratio = d.pop("bluff_combos_ratio", UNSET)

        partner_hands = cast(list[str], d.pop("partner_hands", UNSET))


        _flop_version = d.pop("flop_version", UNSET)
        flop_version: ProjectedRangeRequestFlopVersion | Unset
        if isinstance(_flop_version,  Unset):
            flop_version = UNSET
        else:
            flop_version = ProjectedRangeRequestFlopVersion(_flop_version)




        projected_range_request = cls(
            board=board,
            pot_type=pot_type,
            positions=positions,
            node_id=node_id,
            normalize=normalize,
            bluff_discount_ratio=bluff_discount_ratio,
            hero_position=hero_position,
            hero_hand=hero_hand,
            bluff_combos_ratio=bluff_combos_ratio,
            partner_hands=partner_hands,
            flop_version=flop_version,
        )


        projected_range_request.additional_properties = d
        return projected_range_request

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
