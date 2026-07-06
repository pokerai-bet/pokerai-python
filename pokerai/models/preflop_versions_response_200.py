from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.preflop_versions_response_200_versions_item import PreflopVersionsResponse200VersionsItem





T = TypeVar("T", bound="PreflopVersionsResponse200")



@_attrs_define
class PreflopVersionsResponse200:
    """ 
        Attributes:
            versions (list[PreflopVersionsResponse200VersionsItem] | Unset):
            default (str | Unset): the id used when preflop_version is omitted
     """

    versions: list[PreflopVersionsResponse200VersionsItem] | Unset = UNSET
    default: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.preflop_versions_response_200_versions_item import PreflopVersionsResponse200VersionsItem
        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)



        default = self.default


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if versions is not UNSET:
            field_dict["versions"] = versions
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_versions_response_200_versions_item import PreflopVersionsResponse200VersionsItem
        d = dict(src_dict)
        _versions = d.pop("versions", UNSET)
        versions: list[PreflopVersionsResponse200VersionsItem] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = PreflopVersionsResponse200VersionsItem.from_dict(versions_item_data)



                versions.append(versions_item)


        default = d.pop("default", UNSET)

        preflop_versions_response_200 = cls(
            versions=versions,
            default=default,
        )


        preflop_versions_response_200.additional_properties = d
        return preflop_versions_response_200

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
