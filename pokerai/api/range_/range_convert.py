from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.range_request import RangeRequest
from ...models.range_response import RangeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RangeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/range",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, RangeResponse]]:
    if response.status_code == 200:
        response_200 = RangeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, RangeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RangeRequest,
) -> Response[Union[Error, RangeResponse]]:
    """Range conversion — update ranges along an action line

     Thin proxy to the solver's /api/range. You assemble all inputs including solver_results (the
    decision tree). Charges 1 presolved quota. Output ranges feed the next street's solve.

    Args:
        body (RangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RangeResponse]]
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
    body: RangeRequest,
) -> Optional[Union[Error, RangeResponse]]:
    """Range conversion — update ranges along an action line

     Thin proxy to the solver's /api/range. You assemble all inputs including solver_results (the
    decision tree). Charges 1 presolved quota. Output ranges feed the next street's solve.

    Args:
        body (RangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RangeResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RangeRequest,
) -> Response[Union[Error, RangeResponse]]:
    """Range conversion — update ranges along an action line

     Thin proxy to the solver's /api/range. You assemble all inputs including solver_results (the
    decision tree). Charges 1 presolved quota. Output ranges feed the next street's solve.

    Args:
        body (RangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RangeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RangeRequest,
) -> Optional[Union[Error, RangeResponse]]:
    """Range conversion — update ranges along an action line

     Thin proxy to the solver's /api/range. You assemble all inputs including solver_results (the
    decision tree). Charges 1 presolved quota. Output ranges feed the next street's solve.

    Args:
        body (RangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RangeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
