from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preflop_range_body_preflop_version import PreflopRangeBodyPreflopVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preflop_range_body_positions import PreflopRangeBodyPositions
    from ..models.preflop_range_body_preflop_actions_item import PreflopRangeBodyPreflopActionsItem


T = TypeVar("T", bound="PreflopRangeBody")


@_attrs_define
class PreflopRangeBody:
    """
    Attributes:
        table_size (str):  Example: 6max.
        positions (PreflopRangeBodyPositions):
        preflop_actions (list['PreflopRangeBodyPreflopActionsItem']): full action sequence from SB/BB, same as
            /v1/gto/preflop
        preflop_version (Union[Unset, PreflopRangeBodyPreflopVersion]): optional; which 6max preflop chart set to use
            (same as /v1/gto/preflop). Omit for the default.
    """

    table_size: str
    positions: "PreflopRangeBodyPositions"
    preflop_actions: list["PreflopRangeBodyPreflopActionsItem"]
    preflop_version: Union[Unset, PreflopRangeBodyPreflopVersion] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_size = self.table_size

        positions = self.positions.to_dict()

        preflop_actions = []
        for preflop_actions_item_data in self.preflop_actions:
            preflop_actions_item = preflop_actions_item_data.to_dict()
            preflop_actions.append(preflop_actions_item)

        preflop_version: Union[Unset, str] = UNSET
        if not isinstance(self.preflop_version, Unset):
            preflop_version = self.preflop_version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table_size": table_size,
                "positions": positions,
                "preflop_actions": preflop_actions,
            }
        )
        if preflop_version is not UNSET:
            field_dict["preflop_version"] = preflop_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_body_positions import PreflopRangeBodyPositions
        from ..models.preflop_range_body_preflop_actions_item import PreflopRangeBodyPreflopActionsItem

        d = dict(src_dict)
        table_size = d.pop("table_size")

        positions = PreflopRangeBodyPositions.from_dict(d.pop("positions"))

        preflop_actions = []
        _preflop_actions = d.pop("preflop_actions")
        for preflop_actions_item_data in _preflop_actions:
            preflop_actions_item = PreflopRangeBodyPreflopActionsItem.from_dict(preflop_actions_item_data)

            preflop_actions.append(preflop_actions_item)

        _preflop_version = d.pop("preflop_version", UNSET)
        preflop_version: Union[Unset, PreflopRangeBodyPreflopVersion]
        if isinstance(_preflop_version, Unset):
            preflop_version = UNSET
        else:
            preflop_version = PreflopRangeBodyPreflopVersion(_preflop_version)

        preflop_range_body = cls(
            table_size=table_size,
            positions=positions,
            preflop_actions=preflop_actions,
            preflop_version=preflop_version,
        )

        preflop_range_body.additional_properties = d
        return preflop_range_body

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
