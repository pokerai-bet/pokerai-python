from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayRequest")


@_attrs_define
class ReplayRequest:
    """
    Attributes:
        text (Union[None, Unset, str]): a .phh string; OR supply the config+actions fields below
        variant (Union[None, Unset, str]):
        starting_stacks (Union[None, Unset, list[int]]):
        antes (Union[None, Unset, list[int]]):
        blinds_or_straddles (Union[None, Unset, list[int]]):
        bring_in (Union[None, Unset, int]):
        small_bet (Union[None, Unset, int]):
        big_bet (Union[None, Unset, int]):
        min_bet (Union[None, Unset, int]):
        ante_trimming_status (Union[Unset, bool]):  Default: False.
        automations (Union[None, Unset, list[str]]):
        actions (Union[Unset, list[str]]):
        index (Union[None, Unset, int]): return only the snapshot at this step index
    """

    text: Union[None, Unset, str] = UNSET
    variant: Union[None, Unset, str] = UNSET
    starting_stacks: Union[None, Unset, list[int]] = UNSET
    antes: Union[None, Unset, list[int]] = UNSET
    blinds_or_straddles: Union[None, Unset, list[int]] = UNSET
    bring_in: Union[None, Unset, int] = UNSET
    small_bet: Union[None, Unset, int] = UNSET
    big_bet: Union[None, Unset, int] = UNSET
    min_bet: Union[None, Unset, int] = UNSET
    ante_trimming_status: Union[Unset, bool] = False
    automations: Union[None, Unset, list[str]] = UNSET
    actions: Union[Unset, list[str]] = UNSET
    index: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        variant: Union[None, Unset, str]
        if isinstance(self.variant, Unset):
            variant = UNSET
        else:
            variant = self.variant

        starting_stacks: Union[None, Unset, list[int]]
        if isinstance(self.starting_stacks, Unset):
            starting_stacks = UNSET
        elif isinstance(self.starting_stacks, list):
            starting_stacks = self.starting_stacks

        else:
            starting_stacks = self.starting_stacks

        antes: Union[None, Unset, list[int]]
        if isinstance(self.antes, Unset):
            antes = UNSET
        elif isinstance(self.antes, list):
            antes = self.antes

        else:
            antes = self.antes

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

        index: Union[None, Unset, int]
        if isinstance(self.index, Unset):
            index = UNSET
        else:
            index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if variant is not UNSET:
            field_dict["variant"] = variant
        if starting_stacks is not UNSET:
            field_dict["starting_stacks"] = starting_stacks
        if antes is not UNSET:
            field_dict["antes"] = antes
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
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_variant(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        variant = _parse_variant(d.pop("variant", UNSET))

        def _parse_starting_stacks(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                starting_stacks_type_0 = cast(list[int], data)

                return starting_stacks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        starting_stacks = _parse_starting_stacks(d.pop("starting_stacks", UNSET))

        def _parse_antes(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                antes_type_0 = cast(list[int], data)

                return antes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        antes = _parse_antes(d.pop("antes", UNSET))

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

        def _parse_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index = _parse_index(d.pop("index", UNSET))

        replay_request = cls(
            text=text,
            variant=variant,
            starting_stacks=starting_stacks,
            antes=antes,
            blinds_or_straddles=blinds_or_straddles,
            bring_in=bring_in,
            small_bet=small_bet,
            big_bet=big_bet,
            min_bet=min_bet,
            ante_trimming_status=ante_trimming_status,
            automations=automations,
            actions=actions,
            index=index,
        )

        replay_request.additional_properties = d
        return replay_request

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
