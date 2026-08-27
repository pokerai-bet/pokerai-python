from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.solver_schedule_response_status import SolverScheduleResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota import Quota


T = TypeVar("T", bound="SolverScheduleResponse")


@_attrs_define
class SolverScheduleResponse:
    """
    Attributes:
        status (Union[Unset, SolverScheduleResponseStatus]):
        solve (Union[Unset, str]): handle for /tree and /node
        solve_quota (Union[Unset, Quota]):
    """

    status: Union[Unset, SolverScheduleResponseStatus] = UNSET
    solve: Union[Unset, str] = UNSET
    solve_quota: Union[Unset, "Quota"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        solve = self.solve

        solve_quota: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.solve_quota, Unset):
            solve_quota = self.solve_quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if solve is not UNSET:
            field_dict["solve"] = solve
        if solve_quota is not UNSET:
            field_dict["solve_quota"] = solve_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota import Quota

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, SolverScheduleResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SolverScheduleResponseStatus(_status)

        solve = d.pop("solve", UNSET)

        _solve_quota = d.pop("solve_quota", UNSET)
        solve_quota: Union[Unset, Quota]
        if isinstance(_solve_quota, Unset):
            solve_quota = UNSET
        else:
            solve_quota = Quota.from_dict(_solve_quota)

        solver_schedule_response = cls(
            status=status,
            solve=solve,
            solve_quota=solve_quota,
        )

        solver_schedule_response.additional_properties = d
        return solver_schedule_response

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
