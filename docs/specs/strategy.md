# Strategy port

`trade_desk.strategy.port.Strategy` is venue-agnostic.

A strategy:

- declares `id`, `display_name`, `underlyings`, `mode`
- receives `on_quote` / `on_fill`
- exposes `pending_intents()` (`add`, `close`, `flatten`) — not broker orders
- exposes `view_model()` for its own UI page

It must not import a broker adapter. The engine turns intents into `MultilegOrder`s.

New strategy = new package under `strategies/` plus `docs/strategies/<id>/`.
