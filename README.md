# pokerai-bet

Official Python client for the **[Pokerai API](https://pokerai.bet)** — solver-grade GTO strategy
for 6-max No-Limit Hold'em, over HTTP. Typed, `httpx`-based, **auto-generated from the
[OpenAPI spec](https://pokerai.bet/openapi.yaml)** so it always tracks the live API.

Get a free API key at **https://pokerai.bet/login**. Docs: https://pokerai.bet/docs.en

```bash
pip install pokerai-bet   # distribution name; import as `pokerai`
```

## Quickstart

Preflop GTO strategy for a hand facing an action line:

```python
from pokerai import AuthenticatedClient
from pokerai.api.lookup import preflop_strategy
from pokerai.models import (
    PreflopRequest,
    PreflopRequestPositions,
    PreflopRequestPreflopActionsItem,
    PreflopRequestPreflopActionsItemAction as Act,
)
from pokerai.models.position import Position

client = AuthenticatedClient(base_url="https://pokerai.bet", token="gto_your_key")

req = PreflopRequest(
    hole_cards="AhKh",
    positions=PreflopRequestPositions(hero=Position.MP),
    preflop_actions=[
        PreflopRequestPreflopActionsItem(position=Position.SB, action=Act.SMALL_BLIND, amount=0.5),
        PreflopRequestPreflopActionsItem(position=Position.BB, action=Act.BIG_BLIND, amount=1),
        PreflopRequestPreflopActionsItem(position=Position.UTG, action=Act.RAISE, amount=3),
    ],
)

result = preflop_strategy.sync(client=client, body=req)
print(result)   # situation="Raise", strategy=[{action:"raise", frequency:1.0, amount_bb:9, ...}]
```

## Layout

Every endpoint is a module under `pokerai.api.<tag>` with four functions:

| function | blocking? | returns |
|----------|-----------|---------|
| `sync` | yes | parsed model (or `None`) |
| `sync_detailed` | yes | full `Response` (status + parsed) |
| `asyncio` | no | parsed model |
| `asyncio_detailed` | no | full `Response` |

Tags: `lookup` (preflop + flop presolved), `solver` (real-time turn/river), `range` (range updates).
Request/response models live in `pokerai.models`. Auth is your API key via
`AuthenticatedClient(token=...)` (sent as `Authorization: Bearer`).

## Not into constructing model objects?

This client is fully typed but verbose (it's generated). If you'd rather drive the API from an LLM
agent, see **[@pokerai/mcp](https://www.npmjs.com/package/@pokerai/mcp)** — the same API as MCP tools.
Or call the HTTP endpoints directly; see the [reference](https://pokerai.bet/reference).

MIT licensed.
