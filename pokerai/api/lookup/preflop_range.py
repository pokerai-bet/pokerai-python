from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.preflop_range_body import PreflopRangeBody
from ...models.preflop_range_response_200 import PreflopRangeResponse200
from typing import cast



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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PreflopRangeResponse200 | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PreflopRangeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreflopRangeBody,

) -> Response[Error | PreflopRangeResponse200]:
    """ Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreflopRangeResponse200]
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
    client: AuthenticatedClient | Client,
    body: PreflopRangeBody,

) -> Error | PreflopRangeResponse200 | None:
    """ Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreflopRangeResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreflopRangeBody,

) -> Response[Error | PreflopRangeResponse200]:
    """ Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreflopRangeResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PreflopRangeBody,

) -> Error | PreflopRangeResponse200 | None:
    """ Whole preflop range for a spot (presolved)

     The full 13×13 preflop range for a position + action line in one call — 169 hand types →
    fold/call/raise frequencies. No `hole_cards` (the spot comes from positions +
    preflop_actions). Charges 1 presolved quota (one call, not 169). For a range grid.

    Args:
        body (PreflopRangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreflopRangeResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
