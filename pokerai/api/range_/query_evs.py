from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.evs_request import EvsRequest
from ...models.evs_response import EvsResponse
from typing import cast



def _get_kwargs(
    *,
    body: EvsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/evs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | EvsResponse | None:
    if response.status_code == 200:
        response_200 = EvsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | EvsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EvsRequest,

) -> Response[Any | Error | EvsResponse]:
    """ Node EVs — per-hand, per-action expected values of a completed solve (free)

     Per-hand, per-action expected values at one node of a completed solve. Give the solve handle (from
    /v1/gto/solver) + a node_id (from /v1/gto/solver/tree); optional hand filters to one hand. Free
    (already charged via /v1/gto/solver). Poll /v1/gto/solver/tree until queryable first.

    Args:
        body (EvsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | EvsResponse]
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
    body: EvsRequest,

) -> Any | Error | EvsResponse | None:
    """ Node EVs — per-hand, per-action expected values of a completed solve (free)

     Per-hand, per-action expected values at one node of a completed solve. Give the solve handle (from
    /v1/gto/solver) + a node_id (from /v1/gto/solver/tree); optional hand filters to one hand. Free
    (already charged via /v1/gto/solver). Poll /v1/gto/solver/tree until queryable first.

    Args:
        body (EvsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | EvsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EvsRequest,

) -> Response[Any | Error | EvsResponse]:
    """ Node EVs — per-hand, per-action expected values of a completed solve (free)

     Per-hand, per-action expected values at one node of a completed solve. Give the solve handle (from
    /v1/gto/solver) + a node_id (from /v1/gto/solver/tree); optional hand filters to one hand. Free
    (already charged via /v1/gto/solver). Poll /v1/gto/solver/tree until queryable first.

    Args:
        body (EvsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | EvsResponse]
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
    body: EvsRequest,

) -> Any | Error | EvsResponse | None:
    """ Node EVs — per-hand, per-action expected values of a completed solve (free)

     Per-hand, per-action expected values at one node of a completed solve. Give the solve handle (from
    /v1/gto/solver) + a node_id (from /v1/gto/solver/tree); optional hand filters to one hand. Free
    (already charged via /v1/gto/solver). Poll /v1/gto/solver/tree until queryable first.

    Args:
        body (EvsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | EvsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
