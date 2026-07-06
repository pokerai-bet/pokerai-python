from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.flop_node_request import FlopNodeRequest
from ...models.node_strategy_response import NodeStrategyResponse
from typing import cast



def _get_kwargs(
    *,
    body: FlopNodeRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/flop/node",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | NodeStrategyResponse | None:
    if response.status_code == 200:
        response_200 = NodeStrategyResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | NodeStrategyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FlopNodeRequest,

) -> Response[Error | NodeStrategyResponse]:
    """ Flop node strategy (presolved) — one decision-tree node

     Per-node strategy for the flop decision tree (free, token-gated). Pass a `node` token minted by POST
    /v1/gto/flop/tree. With hole_cards → that hand's mixed strategy at the node; omit hole_cards → the
    node's whole-range strategy.

    This is how you get EVERY hero flop decision — hero in position, hero facing a bet, or a later
    action: fetch the tree, pick a node where is_hero is true (e.g. root/CHECK/BET_13 = hero faces a bet
    after checking → fold/call/raise), and pass its token here. The root node (root) is hero's first
    decision (OOP check/bet).

    The flop tree is single-street; for turn/river decisions use the solver line (/v1/gto/solver/*).

    Args:
        body (FlopNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NodeStrategyResponse]
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
    body: FlopNodeRequest,

) -> Error | NodeStrategyResponse | None:
    """ Flop node strategy (presolved) — one decision-tree node

     Per-node strategy for the flop decision tree (free, token-gated). Pass a `node` token minted by POST
    /v1/gto/flop/tree. With hole_cards → that hand's mixed strategy at the node; omit hole_cards → the
    node's whole-range strategy.

    This is how you get EVERY hero flop decision — hero in position, hero facing a bet, or a later
    action: fetch the tree, pick a node where is_hero is true (e.g. root/CHECK/BET_13 = hero faces a bet
    after checking → fold/call/raise), and pass its token here. The root node (root) is hero's first
    decision (OOP check/bet).

    The flop tree is single-street; for turn/river decisions use the solver line (/v1/gto/solver/*).

    Args:
        body (FlopNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NodeStrategyResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FlopNodeRequest,

) -> Response[Error | NodeStrategyResponse]:
    """ Flop node strategy (presolved) — one decision-tree node

     Per-node strategy for the flop decision tree (free, token-gated). Pass a `node` token minted by POST
    /v1/gto/flop/tree. With hole_cards → that hand's mixed strategy at the node; omit hole_cards → the
    node's whole-range strategy.

    This is how you get EVERY hero flop decision — hero in position, hero facing a bet, or a later
    action: fetch the tree, pick a node where is_hero is true (e.g. root/CHECK/BET_13 = hero faces a bet
    after checking → fold/call/raise), and pass its token here. The root node (root) is hero's first
    decision (OOP check/bet).

    The flop tree is single-street; for turn/river decisions use the solver line (/v1/gto/solver/*).

    Args:
        body (FlopNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NodeStrategyResponse]
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
    body: FlopNodeRequest,

) -> Error | NodeStrategyResponse | None:
    """ Flop node strategy (presolved) — one decision-tree node

     Per-node strategy for the flop decision tree (free, token-gated). Pass a `node` token minted by POST
    /v1/gto/flop/tree. With hole_cards → that hand's mixed strategy at the node; omit hole_cards → the
    node's whole-range strategy.

    This is how you get EVERY hero flop decision — hero in position, hero facing a bet, or a later
    action: fetch the tree, pick a node where is_hero is true (e.g. root/CHECK/BET_13 = hero faces a bet
    after checking → fold/call/raise), and pass its token here. The root node (root) is hero's first
    decision (OOP check/bet).

    The flop tree is single-street; for turn/river decisions use the solver line (/v1/gto/solver/*).

    Args:
        body (FlopNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NodeStrategyResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
