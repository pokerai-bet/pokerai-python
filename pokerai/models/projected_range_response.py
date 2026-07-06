from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quota import Quota





T = TypeVar("T", bound="ProjectedRangeResponse")



@_attrs_define
class ProjectedRangeResponse:
    """ Same fields as RangeResponse, plus pot_type echoed from the request (17 fields total).

        Attributes:
            range_oop_new (str | Unset): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight
                0..1, default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
            range_ip_new (str | Unset): comma-separated hand:weight. class notation AA/AKs/AKo (high rank first); weight
                0..1, default 1. Example: AA:1,KK,AKs:0.5,72o:0.1.
            range_oop_new_raw (str | Unset):
            range_ip_new_raw (str | Unset):
            range_oop_new_raw_before_normalization (str | Unset):
            range_ip_new_raw_before_normalization (str | Unset):
            hand_ranks_oop (str | Unset): OOP combos by made-hand strength: 'combo:rank,...' (lower rank = stronger), sorted
                by rank ascending. Equal-rank tie order is NOT guaranteed stable across endpoints/runs — do not depend on it.
            hand_ranks_ip (str | Unset): IP analog of hand_ranks_oop.
            hand_bottom_ranks_oop (str | Unset): The weakest bluff_combos_ratio fraction of hand_ranks_oop (bluff
                candidates), same format.
            hand_bottom_ranks_ip (str | Unset): IP analog of hand_bottom_ranks_oop.
            node_id (str | Unset):
            board (list[str] | Unset): community cards returned as an array Example: ['2c', '2h', '2s'].
            path_length (int | Unset):
            bluff_discount_ratio (float | Unset):
            bluff_combos_ratio (float | Unset):
            quota (Quota | Unset):
            pot_type (str | Unset):
     """

    range_oop_new: str | Unset = UNSET
    range_ip_new: str | Unset = UNSET
    range_oop_new_raw: str | Unset = UNSET
    range_ip_new_raw: str | Unset = UNSET
    range_oop_new_raw_before_normalization: str | Unset = UNSET
    range_ip_new_raw_before_normalization: str | Unset = UNSET
    hand_ranks_oop: str | Unset = UNSET
    hand_ranks_ip: str | Unset = UNSET
    hand_bottom_ranks_oop: str | Unset = UNSET
    hand_bottom_ranks_ip: str | Unset = UNSET
    node_id: str | Unset = UNSET
    board: list[str] | Unset = UNSET
    path_length: int | Unset = UNSET
    bluff_discount_ratio: float | Unset = UNSET
    bluff_combos_ratio: float | Unset = UNSET
    quota: Quota | Unset = UNSET
    pot_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.quota import Quota
        range_oop_new = self.range_oop_new

        range_ip_new = self.range_ip_new

        range_oop_new_raw = self.range_oop_new_raw

        range_ip_new_raw = self.range_ip_new_raw

        range_oop_new_raw_before_normalization = self.range_oop_new_raw_before_normalization

        range_ip_new_raw_before_normalization = self.range_ip_new_raw_before_normalization

        hand_ranks_oop = self.hand_ranks_oop

        hand_ranks_ip = self.hand_ranks_ip

        hand_bottom_ranks_oop = self.hand_bottom_ranks_oop

        hand_bottom_ranks_ip = self.hand_bottom_ranks_ip

        node_id = self.node_id

        board: list[str] | Unset = UNSET
        if not isinstance(self.board, Unset):
            board = self.board



        path_length = self.path_length

        bluff_discount_ratio = self.bluff_discount_ratio

        bluff_combos_ratio = self.bluff_combos_ratio

        quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()

        pot_type = self.pot_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if range_oop_new is not UNSET:
            field_dict["range_oop_new"] = range_oop_new
        if range_ip_new is not UNSET:
            field_dict["range_ip_new"] = range_ip_new
        if range_oop_new_raw is not UNSET:
            field_dict["range_oop_new_raw"] = range_oop_new_raw
        if range_ip_new_raw is not UNSET:
            field_dict["range_ip_new_raw"] = range_ip_new_raw
        if range_oop_new_raw_before_normalization is not UNSET:
            field_dict["range_oop_new_raw_before_normalization"] = range_oop_new_raw_before_normalization
        if range_ip_new_raw_before_normalization is not UNSET:
            field_dict["range_ip_new_raw_before_normalization"] = range_ip_new_raw_before_normalization
        if hand_ranks_oop is not UNSET:
            field_dict["hand_ranks_oop"] = hand_ranks_oop
        if hand_ranks_ip is not UNSET:
            field_dict["hand_ranks_ip"] = hand_ranks_ip
        if hand_bottom_ranks_oop is not UNSET:
            field_dict["hand_bottom_ranks_oop"] = hand_bottom_ranks_oop
        if hand_bottom_ranks_ip is not UNSET:
            field_dict["hand_bottom_ranks_ip"] = hand_bottom_ranks_ip
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if board is not UNSET:
            field_dict["board"] = board
        if path_length is not UNSET:
            field_dict["path_length"] = path_length
        if bluff_discount_ratio is not UNSET:
            field_dict["bluff_discount_ratio"] = bluff_discount_ratio
        if bluff_combos_ratio is not UNSET:
            field_dict["bluff_combos_ratio"] = bluff_combos_ratio
        if quota is not UNSET:
            field_dict["quota"] = quota
        if pot_type is not UNSET:
            field_dict["pot_type"] = pot_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota import Quota
        d = dict(src_dict)
        range_oop_new = d.pop("range_oop_new", UNSET)

        range_ip_new = d.pop("range_ip_new", UNSET)

        range_oop_new_raw = d.pop("range_oop_new_raw", UNSET)

        range_ip_new_raw = d.pop("range_ip_new_raw", UNSET)

        range_oop_new_raw_before_normalization = d.pop("range_oop_new_raw_before_normalization", UNSET)

        range_ip_new_raw_before_normalization = d.pop("range_ip_new_raw_before_normalization", UNSET)

        hand_ranks_oop = d.pop("hand_ranks_oop", UNSET)

        hand_ranks_ip = d.pop("hand_ranks_ip", UNSET)

        hand_bottom_ranks_oop = d.pop("hand_bottom_ranks_oop", UNSET)

        hand_bottom_ranks_ip = d.pop("hand_bottom_ranks_ip", UNSET)

        node_id = d.pop("node_id", UNSET)

        board = cast(list[str], d.pop("board", UNSET))


        path_length = d.pop("path_length", UNSET)

        bluff_discount_ratio = d.pop("bluff_discount_ratio", UNSET)

        bluff_combos_ratio = d.pop("bluff_combos_ratio", UNSET)

        _quota = d.pop("quota", UNSET)
        quota: Quota | Unset
        if isinstance(_quota,  Unset):
            quota = UNSET
        else:
            quota = Quota.from_dict(_quota)




        pot_type = d.pop("pot_type", UNSET)

        projected_range_response = cls(
            range_oop_new=range_oop_new,
            range_ip_new=range_ip_new,
            range_oop_new_raw=range_oop_new_raw,
            range_ip_new_raw=range_ip_new_raw,
            range_oop_new_raw_before_normalization=range_oop_new_raw_before_normalization,
            range_ip_new_raw_before_normalization=range_ip_new_raw_before_normalization,
            hand_ranks_oop=hand_ranks_oop,
            hand_ranks_ip=hand_ranks_ip,
            hand_bottom_ranks_oop=hand_bottom_ranks_oop,
            hand_bottom_ranks_ip=hand_bottom_ranks_ip,
            node_id=node_id,
            board=board,
            path_length=path_length,
            bluff_discount_ratio=bluff_discount_ratio,
            bluff_combos_ratio=bluff_combos_ratio,
            quota=quota,
            pot_type=pot_type,
        )


        projected_range_response.additional_properties = d
        return projected_range_response

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
