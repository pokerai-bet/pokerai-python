from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.solver_tree_body import SolverTreeBody
from ...models.solver_tree_response import SolverTreeResponse
from typing import cast



def _get_kwargs(
    *,
    body: SolverTreeBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/solver/tree",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SolverTreeResponse | None:
    if response.status_code == 200:
        response_200 = SolverTreeResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SolverTreeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SolverTreeBody,

) -> Response[Error | SolverTreeResponse]:
    """ Poll the solve tree + node status (free)

     Poll until spot_status = queryable. To advance a multi-street solve to the dealt runout, pass
    the dealt cards: `turn_card` (e.g. a flop solve → a specific turn), and/or `river_card`.
    A river spot from a *flop* solve needs BOTH `turn_card` and `river_card` to be unique;
    a turn solve needs only `river_card`. Omit both to get the solve's own street.

    Args:
        body (SolverTreeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SolverTreeResponse]
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
    body: SolverTreeBody,

) -> Error | SolverTreeResponse | None:
    """ Poll the solve tree + node status (free)

     Poll until spot_status = queryable. To advance a multi-street solve to the dealt runout, pass
    the dealt cards: `turn_card` (e.g. a flop solve → a specific turn), and/or `river_card`.
    A river spot from a *flop* solve needs BOTH `turn_card` and `river_card` to be unique;
    a turn solve needs only `river_card`. Omit both to get the solve's own street.

    Args:
        body (SolverTreeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SolverTreeResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SolverTreeBody,

) -> Response[Error | SolverTreeResponse]:
    """ Poll the solve tree + node status (free)

     Poll until spot_status = queryable. To advance a multi-street solve to the dealt runout, pass
    the dealt cards: `turn_card` (e.g. a flop solve → a specific turn), and/or `river_card`.
    A river spot from a *flop* solve needs BOTH `turn_card` and `river_card` to be unique;
    a turn solve needs only `river_card`. Omit both to get the solve's own street.

    Args:
        body (SolverTreeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SolverTreeResponse]
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
    body: SolverTreeBody,

) -> Error | SolverTreeResponse | None:
    """ Poll the solve tree + node status (free)

     Poll until spot_status = queryable. To advance a multi-street solve to the dealt runout, pass
    the dealt cards: `turn_card` (e.g. a flop solve → a specific turn), and/or `river_card`.
    A river spot from a *flop* solve needs BOTH `turn_card` and `river_card` to be unique;
    a turn solve needs only `river_card`. Omit both to get the solve's own street.

    Args:
        body (SolverTreeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SolverTreeResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
