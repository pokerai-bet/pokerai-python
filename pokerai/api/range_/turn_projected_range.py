from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.range_response import RangeResponse
from ...models.turn_projected_range_request import TurnProjectedRangeRequest
from ...models.turn_projected_range_response_200_type_1 import TurnProjectedRangeResponse200Type1
from ...types import Response


def _get_kwargs(
    *,
    body: TurnProjectedRangeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/gto/turn/projected-range",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RangeResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = TurnProjectedRangeResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TurnProjectedRangeRequest,
) -> Response[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    """Projected range — turn→river range update along a turn action line (free)

     The turn→river analog of /v1/gto/flop/projected-range, for a real-time turn solve. Narrows the
    entering-turn ranges (the ranges the solve was scheduled with, read from the solve's own config)
    along a turn action line — including the street-closing CALL/CHECK — to the entering-river ranges.
    Free (the solve was already charged via /v1/gto/solver), like /v1/gto/solver/tree. Returns the same
    range-update output as /v1/gto/range. Poll /v1/gto/solver/tree until spot_status = queryable first.

    Args:
        body (TurnProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['RangeResponse', 'TurnProjectedRangeResponse200Type1']]]
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
    body: TurnProjectedRangeRequest,
) -> Optional[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    """Projected range — turn→river range update along a turn action line (free)

     The turn→river analog of /v1/gto/flop/projected-range, for a real-time turn solve. Narrows the
    entering-turn ranges (the ranges the solve was scheduled with, read from the solve's own config)
    along a turn action line — including the street-closing CALL/CHECK — to the entering-river ranges.
    Free (the solve was already charged via /v1/gto/solver), like /v1/gto/solver/tree. Returns the same
    range-update output as /v1/gto/range. Poll /v1/gto/solver/tree until spot_status = queryable first.

    Args:
        body (TurnProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['RangeResponse', 'TurnProjectedRangeResponse200Type1']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TurnProjectedRangeRequest,
) -> Response[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    """Projected range — turn→river range update along a turn action line (free)

     The turn→river analog of /v1/gto/flop/projected-range, for a real-time turn solve. Narrows the
    entering-turn ranges (the ranges the solve was scheduled with, read from the solve's own config)
    along a turn action line — including the street-closing CALL/CHECK — to the entering-river ranges.
    Free (the solve was already charged via /v1/gto/solver), like /v1/gto/solver/tree. Returns the same
    range-update output as /v1/gto/range. Poll /v1/gto/solver/tree until spot_status = queryable first.

    Args:
        body (TurnProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['RangeResponse', 'TurnProjectedRangeResponse200Type1']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TurnProjectedRangeRequest,
) -> Optional[Union[Error, Union["RangeResponse", "TurnProjectedRangeResponse200Type1"]]]:
    """Projected range — turn→river range update along a turn action line (free)

     The turn→river analog of /v1/gto/flop/projected-range, for a real-time turn solve. Narrows the
    entering-turn ranges (the ranges the solve was scheduled with, read from the solve's own config)
    along a turn action line — including the street-closing CALL/CHECK — to the entering-river ranges.
    Free (the solve was already charged via /v1/gto/solver), like /v1/gto/solver/tree. Returns the same
    range-update output as /v1/gto/range. Poll /v1/gto/solver/tree until spot_status = queryable first.

    Args:
        body (TurnProjectedRangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['RangeResponse', 'TurnProjectedRangeResponse200Type1']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
