from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position import Position
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopPositions")


@_attrs_define
class FlopPositions:
    """required keys depend on pot_type — SRP: hero,raiser,caller; 3BET/4BET: hero,raiser,three_bettor (for 4BET, raiser =
    the opener who 4-bet, three_bettor = the 3-bettor who called; no four_bettor key); LIMP: hero,limper. hero must be
    one of the named seats.

        Attributes:
            hero (Union[Unset, Position]):
            raiser (Union[Unset, Position]):
            caller (Union[Unset, Position]):
            three_bettor (Union[Unset, Position]):
            limper (Union[Unset, Position]):
    """

    hero: Union[Unset, Position] = UNSET
    raiser: Union[Unset, Position] = UNSET
    caller: Union[Unset, Position] = UNSET
    three_bettor: Union[Unset, Position] = UNSET
    limper: Union[Unset, Position] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero: Union[Unset, str] = UNSET
        if not isinstance(self.hero, Unset):
            hero = self.hero.value

        raiser: Union[Unset, str] = UNSET
        if not isinstance(self.raiser, Unset):
            raiser = self.raiser.value

        caller: Union[Unset, str] = UNSET
        if not isinstance(self.caller, Unset):
            caller = self.caller.value

        three_bettor: Union[Unset, str] = UNSET
        if not isinstance(self.three_bettor, Unset):
            three_bettor = self.three_bettor.value

        limper: Union[Unset, str] = UNSET
        if not isinstance(self.limper, Unset):
            limper = self.limper.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero is not UNSET:
            field_dict["hero"] = hero
        if raiser is not UNSET:
            field_dict["raiser"] = raiser
        if caller is not UNSET:
            field_dict["caller"] = caller
        if three_bettor is not UNSET:
            field_dict["three_bettor"] = three_bettor
        if limper is not UNSET:
            field_dict["limper"] = limper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hero = d.pop("hero", UNSET)
        hero: Union[Unset, Position]
        if isinstance(_hero, Unset):
            hero = UNSET
        else:
            hero = Position(_hero)

        _raiser = d.pop("raiser", UNSET)
        raiser: Union[Unset, Position]
        if isinstance(_raiser, Unset):
            raiser = UNSET
        else:
            raiser = Position(_raiser)

        _caller = d.pop("caller", UNSET)
        caller: Union[Unset, Position]
        if isinstance(_caller, Unset):
            caller = UNSET
        else:
            caller = Position(_caller)

        _three_bettor = d.pop("three_bettor", UNSET)
        three_bettor: Union[Unset, Position]
        if isinstance(_three_bettor, Unset):
            three_bettor = UNSET
        else:
            three_bettor = Position(_three_bettor)

        _limper = d.pop("limper", UNSET)
        limper: Union[Unset, Position]
        if isinstance(_limper, Unset):
            limper = UNSET
        else:
            limper = Position(_limper)

        flop_positions = cls(
            hero=hero,
            raiser=raiser,
            caller=caller,
            three_bettor=three_bettor,
            limper=limper,
        )

        flop_positions.additional_properties = d
        return flop_positions

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
