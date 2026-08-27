from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preflop_range_body import PreflopRangeBody
from ...models.preflop_range_response_200 import PreflopRangeResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PreflopRangeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/preflop/range",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PreflopRangeResponse200]]:
    if response.status_code == 200:
        response_200 = PreflopRangeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, PreflopRangeResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PreflopRangeBody,
) -> Response[Union[Error, PreflopRangeResponse200]]:
    """Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Set `include_flop_pruning_guarantees: true` to read an offline immutable manifest for a completed
    Flop batch; this is not a live Flop or database query and there is no `flop_context`. The three
    statuses are `complete`, `incomplete_coverage`, and `awaiting_terminal_preflop_action`.
    `always_removed` is conservative: it proves zero weight only across every compatible canonical board
    in that one terminal scenario. It does not replace the board-specific effective range from POST
    /v1/gto/flop/tree.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PreflopRangeResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PreflopRangeBody,
) -> Optional[Union[Error, PreflopRangeResponse200]]:
    """Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Set `include_flop_pruning_guarantees: true` to read an offline immutable manifest for a completed
    Flop batch; this is not a live Flop or database query and there is no `flop_context`. The three
    statuses are `complete`, `incomplete_coverage`, and `awaiting_terminal_preflop_action`.
    `always_removed` is conservative: it proves zero weight only across every compatible canonical board
    in that one terminal scenario. It does not replace the board-specific effective range from POST
    /v1/gto/flop/tree.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PreflopRangeResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PreflopRangeBody,
) -> Response[Union[Error, PreflopRangeResponse200]]:
    """Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Set `include_flop_pruning_guarantees: true` to read an offline immutable manifest for a completed
    Flop batch; this is not a live Flop or database query and there is no `flop_context`. The three
    statuses are `complete`, `incomplete_coverage`, and `awaiting_terminal_preflop_action`.
    `always_removed` is conservative: it proves zero weight only across every compatible canonical board
    in that one terminal scenario. It does not replace the board-specific effective range from POST
    /v1/gto/flop/tree.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PreflopRangeResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PreflopRangeBody,
) -> Optional[Union[Error, PreflopRangeResponse200]]:
    """Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Set `include_flop_pruning_guarantees: true` to read an offline immutable manifest for a completed
    Flop batch; this is not a live Flop or database query and there is no `flop_context`. The three
    statuses are `complete`, `incomplete_coverage`, and `awaiting_terminal_preflop_action`.
    `always_removed` is conservative: it proves zero weight only across every compatible canonical board
    in that one terminal scenario. It does not replace the board-specific effective range from POST
    /v1/gto/flop/tree.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PreflopRangeResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
