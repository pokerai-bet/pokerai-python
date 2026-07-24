from __future__ import annotations

import asyncio as _asyncio
import time
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, TypeVar

import httpx

from .api.solver import solver_schedule
from .client import AuthenticatedClient, Client
from .models.error import Error
from .models.solver_schedule_request import SolverScheduleRequest
from .models.solver_schedule_response import SolverScheduleResponse
from .types import UNSET, Response, Unset


T = TypeVar("T")


class PokeraiAPIError(RuntimeError):
    """Raised when a solver helper receives a terminal API error."""

    def __init__(self, message: str, *, status_code: int | None = None, body: Mapping[str, Any] | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.body = dict(body or {})


@dataclass(frozen=True)
class ReleaseResult:
    ok: bool
    status_code: int | None = None
    body: Mapping[str, Any] | None = None
    error: str | None = None


def retry_after_ms(response: httpx.Response | Response[Any], body: Mapping[str, Any] | None = None, *, fallback_ms: int = 2500) -> int:
    """Return the server-suggested retry delay for busy solver responses."""

    retry_ms = _number(body.get("retry_after_ms") if body else None)
    if retry_ms is not None and retry_ms > 0:
        return int(retry_ms)
    header_value = response.headers.get("Retry-After")
    retry_seconds = _number(header_value)
    if retry_seconds is not None and retry_seconds > 0:
        return int(retry_seconds * 1000)
    return fallback_ms


def schedule_solver_with_retry(
    *,
    client: AuthenticatedClient | Client,
    body: SolverScheduleRequest,
    max_retries: int = 3,
    sleep: Callable[[float], None] = time.sleep,
) -> SolverScheduleResponse:
    """Schedule a solver task and retry only temporary pool-busy 429 responses."""

    for attempt in range(max_retries + 1):
        res = solver_schedule.sync_detailed(client=client, body=body)
        parsed = _parsed_mapping(res.parsed)
        if res.status_code == HTTPStatus.OK and isinstance(res.parsed, SolverScheduleResponse):
            return res.parsed
        if _is_busy_429(res.status_code, parsed) and attempt < max_retries:
            sleep(retry_after_ms(res, parsed) / 1000)
            continue
        raise PokeraiAPIError(
            f"solver schedule failed: HTTP {int(res.status_code)}",
            status_code=int(res.status_code),
            body=parsed,
        )
    raise AssertionError("unreachable")


async def async_schedule_solver_with_retry(
    *,
    client: AuthenticatedClient | Client,
    body: SolverScheduleRequest,
    max_retries: int = 3,
    sleep: Callable[[float], Awaitable[None]] = _asyncio.sleep,
) -> SolverScheduleResponse:
    """Async variant of schedule_solver_with_retry."""

    for attempt in range(max_retries + 1):
        res = await solver_schedule.asyncio_detailed(client=client, body=body)
        parsed = _parsed_mapping(res.parsed)
        if res.status_code == HTTPStatus.OK and isinstance(res.parsed, SolverScheduleResponse):
            return res.parsed
        if _is_busy_429(res.status_code, parsed) and attempt < max_retries:
            await sleep(retry_after_ms(res, parsed) / 1000)
            continue
        raise PokeraiAPIError(
            f"solver schedule failed: HTTP {int(res.status_code)}",
            status_code=int(res.status_code),
            body=parsed,
        )
    raise AssertionError("unreachable")


def release_solver(*, client: AuthenticatedClient | Client, solve: str) -> ReleaseResult:
    """Release a completed solve handle. Raises on terminal release errors."""

    response = client.get_httpx_client().request(
        "post",
        "/v1/gto/solver/release",
        json={"solve": solve},
        headers={"Content-Type": "application/json"},
    )
    body = _response_json(response)
    if 200 <= response.status_code < 300:
        return ReleaseResult(ok=True, status_code=response.status_code, body=body)
    raise PokeraiAPIError(
        f"solver release failed: HTTP {response.status_code}",
        status_code=response.status_code,
        body=body,
    )


async def async_release_solver(*, client: AuthenticatedClient | Client, solve: str) -> ReleaseResult:
    """Async variant of release_solver."""

    response = await client.get_async_httpx_client().request(
        "post",
        "/v1/gto/solver/release",
        json={"solve": solve},
        headers={"Content-Type": "application/json"},
    )
    body = _response_json(response)
    if 200 <= response.status_code < 300:
        return ReleaseResult(ok=True, status_code=response.status_code, body=body)
    raise PokeraiAPIError(
        f"solver release failed: HTTP {response.status_code}",
        status_code=response.status_code,
        body=body,
    )


def release_solver_best_effort(*, client: AuthenticatedClient | Client, solve: str) -> ReleaseResult:
    """Release a solve handle without masking the caller's primary result or exception."""

    try:
        return release_solver(client=client, solve=solve)
    except Exception as exc:
        return ReleaseResult(ok=False, error=str(exc))


async def async_release_solver_best_effort(*, client: AuthenticatedClient | Client, solve: str) -> ReleaseResult:
    """Async variant of release_solver_best_effort."""

    try:
        return await async_release_solver(client=client, solve=solve)
    except Exception as exc:
        return ReleaseResult(ok=False, error=str(exc))


def with_solver(
    *,
    client: AuthenticatedClient | Client,
    body: SolverScheduleRequest,
    use: Callable[[SolverScheduleResponse], T],
    max_retries: int = 3,
) -> T:
    """Schedule a solve, run caller queries, and always best-effort release in finally."""

    scheduled = schedule_solver_with_retry(client=client, body=body, max_retries=max_retries)
    solve = _solve_handle(scheduled)
    try:
        return use(scheduled)
    finally:
        if solve:
            release_solver_best_effort(client=client, solve=solve)


async def async_with_solver(
    *,
    client: AuthenticatedClient | Client,
    body: SolverScheduleRequest,
    use: Callable[[SolverScheduleResponse], Awaitable[T]],
    max_retries: int = 3,
) -> T:
    """Async variant of with_solver."""

    scheduled = await async_schedule_solver_with_retry(client=client, body=body, max_retries=max_retries)
    solve = _solve_handle(scheduled)
    try:
        return await use(scheduled)
    finally:
        if solve:
            await async_release_solver_best_effort(client=client, solve=solve)


def _solve_handle(scheduled: SolverScheduleResponse) -> str:
    solve = scheduled.solve
    return "" if isinstance(solve, Unset) else str(solve or "")


def _is_busy_429(status_code: HTTPStatus | int, body: Mapping[str, Any]) -> bool:
    if int(status_code) != 429:
        return False
    markers = {str(body.get("status") or ""), str(body.get("error") or ""), str(body.get("reason") or "")}
    return bool(markers & {"busy", "solver_pool_busy"})


def _parsed_mapping(parsed: Any) -> dict[str, Any]:
    if parsed is None:
        return {}
    if isinstance(parsed, Error):
        return parsed.to_dict()
    if hasattr(parsed, "to_dict"):
        return parsed.to_dict()
    if isinstance(parsed, Mapping):
        return dict(parsed)
    return {}


def _response_json(response: httpx.Response) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception:
        return {}
    return dict(data) if isinstance(data, Mapping) else {}


def _number(value: Any) -> float | None:
    if value is None or value is UNSET:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
