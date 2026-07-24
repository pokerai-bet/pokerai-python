import unittest

import httpx

from pokerai import AuthenticatedClient, PokeraiAPIError, schedule_solver_with_retry, with_solver
from pokerai.models.solver_schedule_request import SolverScheduleRequest
from pokerai.models.solver_schedule_request_hero import SolverScheduleRequestHero


def _request() -> SolverScheduleRequest:
    return SolverScheduleRequest(
        board="2c2d2h9s",
        oop_range="AA,KK",
        ip_range="QQ,JJ",
        pot=20,
        effective_stack=90,
        hero=SolverScheduleRequestHero.OOP,
    )


class SolverHelpersTests(unittest.TestCase):
    def test_with_solver_releases_after_success(self) -> None:
        calls: list[tuple[str, str]] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append((request.method, request.url.path))
            if request.url.path == "/v1/gto/solver":
                return httpx.Response(200, json={"status": "computing", "solve": "solve-token"})
            if request.url.path == "/v1/gto/solver/release":
                return httpx.Response(200, json={"status": "success", "released": True})
            raise AssertionError(request.url.path)

        client = AuthenticatedClient(base_url="https://pokerai.test", token="gto_test")
        client.set_httpx_client(httpx.Client(base_url="https://pokerai.test", transport=httpx.MockTransport(handler)))

        result = with_solver(client=client, body=_request(), use=lambda scheduled: scheduled.solve)

        self.assertEqual(result, "solve-token")
        self.assertEqual(calls, [("POST", "/v1/gto/solver"), ("POST", "/v1/gto/solver/release")])

    def test_with_solver_releases_after_callback_error(self) -> None:
        calls: list[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request.url.path)
            if request.url.path == "/v1/gto/solver":
                return httpx.Response(200, json={"status": "computing", "solve": "solve-token"})
            if request.url.path == "/v1/gto/solver/release":
                return httpx.Response(200, json={"status": "success", "released": True})
            raise AssertionError(request.url.path)

        client = AuthenticatedClient(base_url="https://pokerai.test", token="gto_test")
        client.set_httpx_client(httpx.Client(base_url="https://pokerai.test", transport=httpx.MockTransport(handler)))

        with self.assertRaisesRegex(RuntimeError, "primary failure"):
            with_solver(
                client=client,
                body=_request(),
                use=lambda _scheduled: (_ for _ in ()).throw(RuntimeError("primary failure")),
            )

        self.assertEqual(calls, ["/v1/gto/solver", "/v1/gto/solver/release"])

    def test_schedule_retries_busy_429_retry_after_ms(self) -> None:
        calls = 0
        sleeps: list[float] = []

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(
                    429,
                    json={"status": "busy", "error": "solver_pool_busy", "retry_after_ms": 750},
                    headers={"Retry-After": "3"},
                )
            return httpx.Response(200, json={"status": "computing", "solve": "solve-token"})

        client = AuthenticatedClient(base_url="https://pokerai.test", token="gto_test")
        client.set_httpx_client(httpx.Client(base_url="https://pokerai.test", transport=httpx.MockTransport(handler)))

        result = schedule_solver_with_retry(client=client, body=_request(), sleep=sleeps.append)

        self.assertEqual(result.solve, "solve-token")
        self.assertEqual(sleeps, [0.75])

    def test_schedule_does_not_retry_quota_429(self) -> None:
        calls = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            return httpx.Response(429, json={"error": "quota_exceeded", "message": "monthly quota exceeded"})

        client = AuthenticatedClient(base_url="https://pokerai.test", token="gto_test")
        client.set_httpx_client(httpx.Client(base_url="https://pokerai.test", transport=httpx.MockTransport(handler)))

        with self.assertRaises(PokeraiAPIError):
            schedule_solver_with_retry(client=client, body=_request(), sleep=lambda _seconds: None)

        self.assertEqual(calls, 1)


if __name__ == "__main__":
    unittest.main()
