from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preflop_range_response_200_flop_pruning_guarantees_basis import (
    PreflopRangeResponse200FlopPruningGuaranteesBasis,
)
from ..models.preflop_range_response_200_flop_pruning_guarantees_status import (
    PreflopRangeResponse200FlopPruningGuaranteesStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0 import (
        PreflopRangeResponse200FlopPruningGuaranteesContinuationType0,
    )


T = TypeVar("T", bound="PreflopRangeResponse200FlopPruningGuarantees")


@_attrs_define
class PreflopRangeResponse200FlopPruningGuarantees:
    """Present only when include_flop_pruning_guarantees was requested. Missing data must not be used to infer a removal
    list.

        Attributes:
            status (Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesStatus]):
            basis (Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesBasis]):
            flop_version (Union[Unset, str]):
            manifest_version (Union[Unset, str]):
            continuation (Union['PreflopRangeResponse200FlopPruningGuaranteesContinuationType0', None, Unset]):
    """

    status: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesStatus] = UNSET
    basis: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesBasis] = UNSET
    flop_version: Union[Unset, str] = UNSET
    manifest_version: Union[Unset, str] = UNSET
    continuation: Union["PreflopRangeResponse200FlopPruningGuaranteesContinuationType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0 import (
            PreflopRangeResponse200FlopPruningGuaranteesContinuationType0,
        )

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        basis: Union[Unset, str] = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis.value

        flop_version = self.flop_version

        manifest_version = self.manifest_version

        continuation: Union[None, Unset, dict[str, Any]]
        if isinstance(self.continuation, Unset):
            continuation = UNSET
        elif isinstance(self.continuation, PreflopRangeResponse200FlopPruningGuaranteesContinuationType0):
            continuation = self.continuation.to_dict()
        else:
            continuation = self.continuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if basis is not UNSET:
            field_dict["basis"] = basis
        if flop_version is not UNSET:
            field_dict["flop_version"] = flop_version
        if manifest_version is not UNSET:
            field_dict["manifest_version"] = manifest_version
        if continuation is not UNSET:
            field_dict["continuation"] = continuation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflop_range_response_200_flop_pruning_guarantees_continuation_type_0 import (
            PreflopRangeResponse200FlopPruningGuaranteesContinuationType0,
        )

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PreflopRangeResponse200FlopPruningGuaranteesStatus(_status)

        _basis = d.pop("basis", UNSET)
        basis: Union[Unset, PreflopRangeResponse200FlopPruningGuaranteesBasis]
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = PreflopRangeResponse200FlopPruningGuaranteesBasis(_basis)

        flop_version = d.pop("flop_version", UNSET)

        manifest_version = d.pop("manifest_version", UNSET)

        def _parse_continuation(
            data: object,
        ) -> Union["PreflopRangeResponse200FlopPruningGuaranteesContinuationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                continuation_type_0 = PreflopRangeResponse200FlopPruningGuaranteesContinuationType0.from_dict(data)

                return continuation_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PreflopRangeResponse200FlopPruningGuaranteesContinuationType0", None, Unset], data)

        continuation = _parse_continuation(d.pop("continuation", UNSET))

        preflop_range_response_200_flop_pruning_guarantees = cls(
            status=status,
            basis=basis,
            flop_version=flop_version,
            manifest_version=manifest_version,
            continuation=continuation,
        )

        preflop_range_response_200_flop_pruning_guarantees.additional_properties = d
        return preflop_range_response_200_flop_pruning_guarantees

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
