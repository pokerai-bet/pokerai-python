from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.range_request_hero_position import RangeRequestHeroPosition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_request_solver_results import RangeRequestSolverResults


T = TypeVar("T", bound="RangeRequest")


@_attrs_define
class RangeRequest:
    """
    Attributes:
        range_oop (str): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1, default
            1. Example: AA:1,KK,AKs:0.5,72o:0.1.
        range_ip (str): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight 0..1, default
            1. Example: AA:1,KK,AKs:0.5,72o:0.1.
        solver_results (RangeRequestSolverResults): the decision tree (you assemble it)
        node_id (str):  Example: root/CHECK/BET 8.000000.
        board (Union[Unset, str]): community cards as a no-separator string: 3=flop "2c2h2s", 4=turn, 5=river. Example:
            2c2h2s.
        normalize (Union[Unset, bool]):  Default: True.
        explain (Union[Unset, bool]):  Default: False.
        track_hands (Union[Unset, list[str]]):
        bluff_discount_ratio (Union[Unset, float]):
        hero_position (Union[Unset, RangeRequestHeroPosition]): optional card blocking: which player is Hero. Pair with
            hero_hand.
        hero_hand (Union[Unset, str]): optional card blocking: remove every combo containing one of Hero's cards from
            the ranges (range-vs-hand analysis). Echoed back in the response. Applies to /v1/gto/range only, not the
            projected-range wrappers. Example: AsKs.
    """

    range_oop: str
    range_ip: str
    solver_results: "RangeRequestSolverResults"
    node_id: str
    board: Union[Unset, str] = UNSET
    normalize: Union[Unset, bool] = True
    explain: Union[Unset, bool] = False
    track_hands: Union[Unset, list[str]] = UNSET
    bluff_discount_ratio: Union[Unset, float] = UNSET
    hero_position: Union[Unset, RangeRequestHeroPosition] = UNSET
    hero_hand: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_oop = self.range_oop

        range_ip = self.range_ip

        solver_results = self.solver_results.to_dict()

        node_id = self.node_id

        board = self.board

        normalize = self.normalize

        explain = self.explain

        track_hands: Union[Unset, list[str]] = UNSET
        if not isinstance(self.track_hands, Unset):
            track_hands = self.track_hands

        bluff_discount_ratio = self.bluff_discount_ratio

        hero_position: Union[Unset, str] = UNSET
        if not isinstance(self.hero_position, Unset):
            hero_position = self.hero_position.value

        hero_hand = self.hero_hand

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range_oop": range_oop,
                "range_ip": range_ip,
                "solver_results": solver_results,
                "node_id": node_id,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if normalize is not UNSET:
            field_dict["normalize"] = normalize
        if explain is not UNSET:
            field_dict["explain"] = explain
        if track_hands is not UNSET:
            field_dict["track_hands"] = track_hands
        if bluff_discount_ratio is not UNSET:
            field_dict["bluff_discount_ratio"] = bluff_discount_ratio
        if hero_position is not UNSET:
            field_dict["hero_position"] = hero_position
        if hero_hand is not UNSET:
            field_dict["hero_hand"] = hero_hand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_request_solver_results import RangeRequestSolverResults

        d = dict(src_dict)
        range_oop = d.pop("range_oop")

        range_ip = d.pop("range_ip")

        solver_results = RangeRequestSolverResults.from_dict(d.pop("solver_results"))

        node_id = d.pop("node_id")

        board = d.pop("board", UNSET)

        normalize = d.pop("normalize", UNSET)

        explain = d.pop("explain", UNSET)

        track_hands = cast(list[str], d.pop("track_hands", UNSET))

        bluff_discount_ratio = d.pop("bluff_discount_ratio", UNSET)

        _hero_position = d.pop("hero_position", UNSET)
        hero_position: Union[Unset, RangeRequestHeroPosition]
        if isinstance(_hero_position, Unset):
            hero_position = UNSET
        else:
            hero_position = RangeRequestHeroPosition(_hero_position)

        hero_hand = d.pop("hero_hand", UNSET)

        range_request = cls(
            range_oop=range_oop,
            range_ip=range_ip,
            solver_results=solver_results,
            node_id=node_id,
            board=board,
            normalize=normalize,
            explain=explain,
            track_hands=track_hands,
            bluff_discount_ratio=bluff_discount_ratio,
            hero_position=hero_position,
            hero_hand=hero_hand,
        )

        range_request.additional_properties = d
        return range_request

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
