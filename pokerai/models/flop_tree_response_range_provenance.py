from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flop_tree_response_range_provenance_effective_source import FlopTreeResponseRangeProvenanceEffectiveSource
from ..models.flop_tree_response_range_provenance_policy_audit_status import (
    FlopTreeResponseRangeProvenancePolicyAuditStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlopTreeResponseRangeProvenance")


@_attrs_define
class FlopTreeResponseRangeProvenance:
    """
    Attributes:
        effective_source (Union[Unset, FlopTreeResponseRangeProvenanceEffectiveSource]):
        policy_audit_status (Union[Unset, FlopTreeResponseRangeProvenancePolicyAuditStatus]): mismatch is historical
            effective-versus-current-policy disagreement, not an artifact/range mismatch.
    """

    effective_source: Union[Unset, FlopTreeResponseRangeProvenanceEffectiveSource] = UNSET
    policy_audit_status: Union[Unset, FlopTreeResponseRangeProvenancePolicyAuditStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_source: Union[Unset, str] = UNSET
        if not isinstance(self.effective_source, Unset):
            effective_source = self.effective_source.value

        policy_audit_status: Union[Unset, str] = UNSET
        if not isinstance(self.policy_audit_status, Unset):
            policy_audit_status = self.policy_audit_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effective_source is not UNSET:
            field_dict["effective_source"] = effective_source
        if policy_audit_status is not UNSET:
            field_dict["policy_audit_status"] = policy_audit_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _effective_source = d.pop("effective_source", UNSET)
        effective_source: Union[Unset, FlopTreeResponseRangeProvenanceEffectiveSource]
        if isinstance(_effective_source, Unset):
            effective_source = UNSET
        else:
            effective_source = FlopTreeResponseRangeProvenanceEffectiveSource(_effective_source)

        _policy_audit_status = d.pop("policy_audit_status", UNSET)
        policy_audit_status: Union[Unset, FlopTreeResponseRangeProvenancePolicyAuditStatus]
        if isinstance(_policy_audit_status, Unset):
            policy_audit_status = UNSET
        else:
            policy_audit_status = FlopTreeResponseRangeProvenancePolicyAuditStatus(_policy_audit_status)

        flop_tree_response_range_provenance = cls(
            effective_source=effective_source,
            policy_audit_status=policy_audit_status,
        )

        flop_tree_response_range_provenance.additional_properties = d
        return flop_tree_response_range_provenance

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
