from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.projected_range_request import ProjectedRangeRequest
from ...models.projected_range_response import ProjectedRangeResponse
from typing import cast



def _get_kwargs(
    *,
    body: ProjectedRangeRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/flop/projected-range",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ProjectedRangeResponse | None:
    if response.status_code == 200:
        response_200 = ProjectedRangeResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ProjectedRangeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectedRangeRequest,

) -> Response[Error | ProjectedRangeResponse]:
    """ Projected range — flop range update along an action line (presolved quota)

     Projects the flop ranges forward along an action line for the given board / pot_type / positions.
    Charges 1 presolved quota. Returns the same range-update output as /v1/gto/range.

    Args:
        body (ProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectedRangeResponse]
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
    body: ProjectedRangeRequest,

) -> Error | ProjectedRangeResponse | None:
    """ Projected range — flop range update along an action line (presolved quota)

     Projects the flop ranges forward along an action line for the given board / pot_type / positions.
    Charges 1 presolved quota. Returns the same range-update output as /v1/gto/range.

    Args:
        body (ProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectedRangeResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectedRangeRequest,

) -> Response[Error | ProjectedRangeResponse]:
    """ Projected range — flop range update along an action line (presolved quota)

     Projects the flop ranges forward along an action line for the given board / pot_type / positions.
    Charges 1 presolved quota. Returns the same range-update output as /v1/gto/range.

    Args:
        body (ProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectedRangeResponse]
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
    body: ProjectedRangeRequest,

) -> Error | ProjectedRangeResponse | None:
    """ Projected range — flop range update along an action line (presolved quota)

     Projects the flop ranges forward along an action line for the given board / pot_type / positions.
    Charges 1 presolved quota. Returns the same range-update output as /v1/gto/range.

    Args:
        body (ProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectedRangeResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
