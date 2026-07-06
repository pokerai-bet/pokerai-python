from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.preflop_versions_response_200 import PreflopVersionsResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/gto/preflop/versions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PreflopVersionsResponse200 | None:
    if response.status_code == 200:
        response_200 = PreflopVersionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PreflopVersionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | PreflopVersionsResponse200]:
    """ List installed preflop strategy versions (free)

     The selectable preflop_version values for /v1/gto/preflop and /v1/gto/preflop/range, with a human
    label for each and which one is the default (used when preflop_version is omitted). Free (no quota).
    Use this instead of hardcoding the list — new versions appear here automatically.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreflopVersionsResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> Error | PreflopVersionsResponse200 | None:
    """ List installed preflop strategy versions (free)

     The selectable preflop_version values for /v1/gto/preflop and /v1/gto/preflop/range, with a human
    label for each and which one is the default (used when preflop_version is omitted). Free (no quota).
    Use this instead of hardcoding the list — new versions appear here automatically.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreflopVersionsResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | PreflopVersionsResponse200]:
    """ List installed preflop strategy versions (free)

     The selectable preflop_version values for /v1/gto/preflop and /v1/gto/preflop/range, with a human
    label for each and which one is the default (used when preflop_version is omitted). Free (no quota).
    Use this instead of hardcoding the list — new versions appear here automatically.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreflopVersionsResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> Error | PreflopVersionsResponse200 | None:
    """ List installed preflop strategy versions (free)

     The selectable preflop_version values for /v1/gto/preflop and /v1/gto/preflop/range, with a human
    label for each and which one is the default (used when preflop_version is omitted). Free (no quota).
    Use this instead of hardcoding the list — new versions appear here automatically.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreflopVersionsResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
