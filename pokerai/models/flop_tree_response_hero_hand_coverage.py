from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flop_tree_response_hero_hand_coverage_status import FlopTreeResponseHeroHandCoverageStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopTreeResponseHeroHandCoverage")


@_attrs_define
class FlopTreeResponseHeroHandCoverage:
    """Present only when hole_cards was requested on the tree.

    Attributes:
        hand (Union[Unset, str]): two cards, no separator, e.g. "AdKd". Rank AKQJT98765432, suit c d h s. Example: AdKd.
        position (Union[Unset, str]):
        requested_weight (Union[Unset, float]):
        effective_weight (Union[Unset, float]):
        status (Union[Unset, FlopTreeResponseHeroHandCoverageStatus]):
    """

    hand: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    requested_weight: Union[Unset, float] = UNSET
    effective_weight: Union[Unset, float] = UNSET
    status: Union[Unset, FlopTreeResponseHeroHandCoverageStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hand = self.hand

        position = self.position

        requested_weight = self.requested_weight

        effective_weight = self.effective_weight

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hand is not UNSET:
            field_dict["hand"] = hand
        if position is not UNSET:
            field_dict["position"] = position
        if requested_weight is not UNSET:
            field_dict["requested_weight"] = requested_weight
        if effective_weight is not UNSET:
            field_dict["effective_weight"] = effective_weight
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hand = d.pop("hand", UNSET)

        position = d.pop("position", UNSET)

        requested_weight = d.pop("requested_weight", UNSET)

        effective_weight = d.pop("effective_weight", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FlopTreeResponseHeroHandCoverageStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FlopTreeResponseHeroHandCoverageStatus(_status)

        flop_tree_response_hero_hand_coverage = cls(
            hand=hand,
            position=position,
            requested_weight=requested_weight,
            effective_weight=effective_weight,
            status=status,
        )

        flop_tree_response_hero_hand_coverage.additional_properties = d
        return flop_tree_response_hero_hand_coverage

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
