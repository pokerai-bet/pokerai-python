from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.icm_request import IcmRequest
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: IcmRequest,
    authorization: Union[Unset, str] = "",
    x_api_key: Union[Unset, str] = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    if not isinstance(x_api_key, Unset):
        headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/pokerkit/icm",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IcmRequest,
    authorization: Union[Unset, str] = "",
    x_api_key: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """Icm

    Args:
        authorization (Union[Unset, str]):  Default: ''.
        x_api_key (Union[Unset, str]):  Default: ''.
        body (IcmRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IcmRequest,
    authorization: Union[Unset, str] = "",
    x_api_key: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Icm

    Args:
        authorization (Union[Unset, str]):  Default: ''.
        x_api_key (Union[Unset, str]):  Default: ''.
        body (IcmRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IcmRequest,
    authorization: Union[Unset, str] = "",
    x_api_key: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """Icm

    Args:
        authorization (Union[Unset, str]):  Default: ''.
        x_api_key (Union[Unset, str]):  Default: ''.
        body (IcmRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IcmRequest,
    authorization: Union[Unset, str] = "",
    x_api_key: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Icm

    Args:
        authorization (Union[Unset, str]):  Default: ''.
        x_api_key (Union[Unset, str]):  Default: ''.
        body (IcmRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_api_key=x_api_key,
        )
    ).parsed
