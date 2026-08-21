# Broker port

`trade_desk.broker.port.Broker` is the only API a strategy/engine may use for a venue.

Required methods:

- `get_quote(symbol)`
- `get_expirations(symbol)`
- `get_chain(symbol, expiration)` — copy OCC symbols from the chain; never invent them
- `preview_multileg(order)`
- `place_multileg(order)` — 4-leg credit/debit, not market, once live
- `get_order(id)` — HTTP 200 on place is not a fill
- `get_positions()`

Adapters live under `src/trade_desk/brokers/<name>/`. The adapter may speak HTTP, FIX, or SDK. It must map to `domain` types only.

Tradier is the first adapter (`id = "tradier"`). Sandbox base URL is delayed; do not use it for 0DTE add triggers.
