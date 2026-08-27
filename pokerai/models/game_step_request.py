from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameStepRequest")


@_attrs_define
class GameStepRequest:
    """
    Attributes:
        variant (str): variant code, e.g. NT (NL hold'em); see /meta
        starting_stacks (list[int]):
        antes (list[int]):
        next_action (str): the player/deal action to apply
        blinds_or_straddles (Union[None, Unset, list[int]]):
        bring_in (Union[None, Unset, int]):
        small_bet (Union[None, Unset, int]):
        big_bet (Union[None, Unset, int]):
        min_bet (Union[None, Unset, int]): required for no-limit/pot-limit, e.g. 2
        ante_trimming_status (Union[Unset, bool]):  Default: False.
        automations (Union[None, Unset, list[str]]): Automation names; omit for pokerkit defaults
        actions (Union[Unset, list[str]]):
        viewer (Union[None, Unset, int]): reserved (hidden-info tier); v1 is full-information
        expected_action_count (Union[None, Unset, int]): optimistic-concurrency token = len(actions) you are extending;
            409 on mismatch
    """

    variant: str
    starting_stacks: list[int]
    antes: list[int]
    next_action: str
    blinds_or_straddles: Union[None, Unset, list[int]] = UNSET
    bring_in: Union[None, Unset, int] = UNSET
    small_bet: Union[None, Unset, int] = UNSET
    big_bet: Union[None, Unset, int] = UNSET
    min_bet: Union[None, Unset, int] = UNSET
    ante_trimming_status: Union[Unset, bool] = False
    automations: Union[None, Unset, list[str]] = UNSET
    actions: Union[Unset, list[str]] = UNSET
    viewer: Union[None, Unset, int] = UNSET
    expected_action_count: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant = self.variant

        starting_stacks = self.starting_stacks

        antes = self.antes

        next_action = self.next_action

        blinds_or_straddles: Union[None, Unset, list[int]]
        if isinstance(self.blinds_or_straddles, Unset):
            blinds_or_straddles = UNSET
        elif isinstance(self.blinds_or_straddles, list):
            blinds_or_straddles = self.blinds_or_straddles

        else:
            blinds_or_straddles = self.blinds_or_straddles

        bring_in: Union[None, Unset, int]
        if isinstance(self.bring_in, Unset):
            bring_in = UNSET
        else:
            bring_in = self.bring_in

        small_bet: Union[None, Unset, int]
        if isinstance(self.small_bet, Unset):
            small_bet = UNSET
        else:
            small_bet = self.small_bet

        big_bet: Union[None, Unset, int]
        if isinstance(self.big_bet, Unset):
            big_bet = UNSET
        else:
            big_bet = self.big_bet

        min_bet: Union[None, Unset, int]
        if isinstance(self.min_bet, Unset):
            min_bet = UNSET
        else:
            min_bet = self.min_bet

        ante_trimming_status = self.ante_trimming_status

        automations: Union[None, Unset, list[str]]
        if isinstance(self.automations, Unset):
            automations = UNSET
        elif isinstance(self.automations, list):
            automations = self.automations

        else:
            automations = self.automations

        actions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        viewer: Union[None, Unset, int]
        if isinstance(self.viewer, Unset):
            viewer = UNSET
        else:
            viewer = self.viewer

        expected_action_count: Union[None, Unset, int]
        if isinstance(self.expected_action_count, Unset):
            expected_action_count = UNSET
        else:
            expected_action_count = self.expected_action_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant": variant,
                "starting_stacks": starting_stacks,
                "antes": antes,
                "next_action": next_action,
            }
        )
        if blinds_or_straddles is not UNSET:
            field_dict["blinds_or_straddles"] = blinds_or_straddles
        if bring_in is not UNSET:
            field_dict["bring_in"] = bring_in
        if small_bet is not UNSET:
            field_dict["small_bet"] = small_bet
        if big_bet is not UNSET:
            field_dict["big_bet"] = big_bet
        if min_bet is not UNSET:
            field_dict["min_bet"] = min_bet
        if ante_trimming_status is not UNSET:
            field_dict["ante_trimming_status"] = ante_trimming_status
        if automations is not UNSET:
            field_dict["automations"] = automations
        if actions is not UNSET:
            field_dict["actions"] = actions
        if viewer is not UNSET:
            field_dict["viewer"] = viewer
        if expected_action_count is not UNSET:
            field_dict["expected_action_count"] = expected_action_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        variant = d.pop("variant")

        starting_stacks = cast(list[int], d.pop("starting_stacks"))

        antes = cast(list[int], d.pop("antes"))

        next_action = d.pop("next_action")

        def _parse_blinds_or_straddles(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blinds_or_straddles_type_0 = cast(list[int], data)

                return blinds_or_straddles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        blinds_or_straddles = _parse_blinds_or_straddles(d.pop("blinds_or_straddles", UNSET))

        def _parse_bring_in(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bring_in = _parse_bring_in(d.pop("bring_in", UNSET))

        def _parse_small_bet(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        small_bet = _parse_small_bet(d.pop("small_bet", UNSET))

        def _parse_big_bet(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        big_bet = _parse_big_bet(d.pop("big_bet", UNSET))

        def _parse_min_bet(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_bet = _parse_min_bet(d.pop("min_bet", UNSET))

        ante_trimming_status = d.pop("ante_trimming_status", UNSET)

        def _parse_automations(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                automations_type_0 = cast(list[str], data)

                return automations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        automations = _parse_automations(d.pop("automations", UNSET))

        actions = cast(list[str], d.pop("actions", UNSET))

        def _parse_viewer(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        viewer = _parse_viewer(d.pop("viewer", UNSET))

        def _parse_expected_action_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        expected_action_count = _parse_expected_action_count(d.pop("expected_action_count", UNSET))

        game_step_request = cls(
            variant=variant,
            starting_stacks=starting_stacks,
            antes=antes,
            next_action=next_action,
            blinds_or_straddles=blinds_or_straddles,
            bring_in=bring_in,
            small_bet=small_bet,
            big_bet=big_bet,
            min_bet=min_bet,
            ante_trimming_status=ante_trimming_status,
            automations=automations,
            actions=actions,
            viewer=viewer,
            expected_action_count=expected_action_count,
        )

        game_step_request.additional_properties = d
        return game_step_request

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
