from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.solver_schedule_request_hero import SolverScheduleRequestHero
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solver_schedule_request_bet_sizes import SolverScheduleRequestBetSizes
    from ..models.solver_schedule_request_donk_sizes import SolverScheduleRequestDonkSizes
    from ..models.solver_schedule_request_raise_sizes import SolverScheduleRequestRaiseSizes


T = TypeVar("T", bound="SolverScheduleRequest")


@_attrs_define
class SolverScheduleRequest:
    """
    Attributes:
        board (str): community cards as a no-separator string: 3=flop "2c2h2s", 4=turn, 5=river. Example: 2c2h2s.
        oop_range (str): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1, default
            1. Example: AA:1,KK,AKs:0.5,72o:0.1.
        ip_range (str): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1, default
            1. Example: AA:1,KK,AKs:0.5,72o:0.1.
        pot (float):
        effective_stack (float):
        hero (SolverScheduleRequestHero):
        bet_sizes (Union[Unset, SolverScheduleRequestBetSizes]): optional per-street opening bet sizes in pot %; flop
            defaults to 50%
        raise_sizes (Union[Unset, SolverScheduleRequestRaiseSizes]): optional per-street raise sizes in pot %; omitted
            streets reuse bet_sizes/defaults
        donk_sizes (Union[Unset, SolverScheduleRequestDonkSizes]): optional OOP donk-lead sizes in pot %; turn defaults
            to 67%, river defaults to 100%
        raise_limit (Union[Unset, int]): optional tree-wide raise cap; defaults to 3 for flop/turn solves and 4 for
            river-only solves
    """

    board: str
    oop_range: str
    ip_range: str
    pot: float
    effective_stack: float
    hero: SolverScheduleRequestHero
    bet_sizes: Union[Unset, "SolverScheduleRequestBetSizes"] = UNSET
    raise_sizes: Union[Unset, "SolverScheduleRequestRaiseSizes"] = UNSET
    donk_sizes: Union[Unset, "SolverScheduleRequestDonkSizes"] = UNSET
    raise_limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board = self.board

        oop_range = self.oop_range

        ip_range = self.ip_range

        pot = self.pot

        effective_stack = self.effective_stack

        hero = self.hero.value

        bet_sizes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bet_sizes, Unset):
            bet_sizes = self.bet_sizes.to_dict()

        raise_sizes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.raise_sizes, Unset):
            raise_sizes = self.raise_sizes.to_dict()

        donk_sizes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.donk_sizes, Unset):
            donk_sizes = self.donk_sizes.to_dict()

        raise_limit = self.raise_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "board": board,
                "oop_range": oop_range,
                "ip_range": ip_range,
                "pot": pot,
                "effective_stack": effective_stack,
                "hero": hero,
            }
        )
        if bet_sizes is not UNSET:
            field_dict["bet_sizes"] = bet_sizes
        if raise_sizes is not UNSET:
            field_dict["raise_sizes"] = raise_sizes
        if donk_sizes is not UNSET:
            field_dict["donk_sizes"] = donk_sizes
        if raise_limit is not UNSET:
            field_dict["raise_limit"] = raise_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.solver_schedule_request_bet_sizes import SolverScheduleRequestBetSizes
        from ..models.solver_schedule_request_donk_sizes import SolverScheduleRequestDonkSizes
        from ..models.solver_schedule_request_raise_sizes import SolverScheduleRequestRaiseSizes

        d = dict(src_dict)
        board = d.pop("board")

        oop_range = d.pop("oop_range")

        ip_range = d.pop("ip_range")

        pot = d.pop("pot")

        effective_stack = d.pop("effective_stack")

        hero = SolverScheduleRequestHero(d.pop("hero"))

        _bet_sizes = d.pop("bet_sizes", UNSET)
        bet_sizes: Union[Unset, SolverScheduleRequestBetSizes]
        if isinstance(_bet_sizes, Unset):
            bet_sizes = UNSET
        else:
            bet_sizes = SolverScheduleRequestBetSizes.from_dict(_bet_sizes)

        _raise_sizes = d.pop("raise_sizes", UNSET)
        raise_sizes: Union[Unset, SolverScheduleRequestRaiseSizes]
        if isinstance(_raise_sizes, Unset):
            raise_sizes = UNSET
        else:
            raise_sizes = SolverScheduleRequestRaiseSizes.from_dict(_raise_sizes)

        _donk_sizes = d.pop("donk_sizes", UNSET)
        donk_sizes: Union[Unset, SolverScheduleRequestDonkSizes]
        if isinstance(_donk_sizes, Unset):
            donk_sizes = UNSET
        else:
            donk_sizes = SolverScheduleRequestDonkSizes.from_dict(_donk_sizes)

        raise_limit = d.pop("raise_limit", UNSET)

        solver_schedule_request = cls(
            board=board,
            oop_range=oop_range,
            ip_range=ip_range,
            pot=pot,
            effective_stack=effective_stack,
            hero=hero,
            bet_sizes=bet_sizes,
            raise_sizes=raise_sizes,
            donk_sizes=donk_sizes,
            raise_limit=raise_limit,
        )

        solver_schedule_request.additional_properties = d
        return solver_schedule_request

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
