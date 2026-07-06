from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.flop_tree_request_flop_version import FlopTreeRequestFlopVersion
from ..models.flop_tree_request_pot_type import FlopTreeRequestPotType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.flop_positions import FlopPositions





T = TypeVar("T", bound="FlopTreeRequest")



@_attrs_define
class FlopTreeRequest:
    """ 
        Attributes:
            board (str): community cards as a no-separator string: 3=flop "2c2h2s", 4=turn, 5=river. Example: 2c2h2s.
            pot_type (FlopTreeRequestPotType):
            positions (FlopPositions): required keys depend on pot_type — SRP: hero,raiser,caller; 3BET/4BET:
                hero,raiser,three_bettor (for 4BET, raiser = the opener who 4-bet, three_bettor = the 3-bettor who called; no
                four_bettor key); LIMP: hero,limper. hero must be one of the named seats.
            flop_version (FlopTreeRequestFlopVersion | Unset): optional; which flop dataset (one solved per preflop
                version). Omit for the default (6max). If the chosen version has no data for the spot the service degrades
                gracefully to 6max. Unknown value -> 400 unsupported_flop_version. Independent of preflop_version. The node
                tokens carry this version, so /v1/gto/flop/node stays on the same dataset.
     """

    board: str
    pot_type: FlopTreeRequestPotType
    positions: FlopPositions
    flop_version: FlopTreeRequestFlopVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.flop_positions import FlopPositions
        board = self.board

        pot_type = self.pot_type.value

        positions = self.positions.to_dict()

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
        if flop_version is not UNSET:
            field_dict["flop_version"] = flop_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flop_positions import FlopPositions
        d = dict(src_dict)
        board = d.pop("board")

        pot_type = FlopTreeRequestPotType(d.pop("pot_type"))




        positions = FlopPositions.from_dict(d.pop("positions"))




        _flop_version = d.pop("flop_version", UNSET)
        flop_version: FlopTreeRequestFlopVersion | Unset
        if isinstance(_flop_version,  Unset):
            flop_version = UNSET
        else:
            flop_version = FlopTreeRequestFlopVersion(_flop_version)




        flop_tree_request = cls(
            board=board,
            pot_type=pot_type,
            positions=positions,
            flop_version=flop_version,
        )


        flop_tree_request.additional_properties = d
        return flop_tree_request

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
