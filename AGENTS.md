# trade-desk for agents

This is a multi-strategy, multi-broker desk. Specs in `docs/specs/` are source of truth. Change the spec before changing ports.

## Hard rules

- Never commit `.env`, tokens, account IDs, live fills, or statements.
- Never import a broker adapter from a strategy package, or a strategy from a broker adapter.
- Iron fly is semi-manual (`confirm`): compute Watch / Next Move / BTC; do not place until the UI confirms.
- Credit 4-leg orders use a limit, not a market, once live sending exists.
- Sandbox quotes are delayed; do not treat them as valid 0DTE add triggers.

## Where to edit

| Change                         | Location |
|--------------------------------|----------|
| Domain types                   | `src/trade_desk/domain/` |
| Broker interface               | `src/trade_desk/broker/port.py` |
| Tradier HTTP                   | `src/trade_desk/brokers/tradier/` |
| Strategy interface             | `src/trade_desk/strategy/port.py` |
| Iron fly rules / Captain's Log | `src/trade_desk/strategies/spx_iron_fly/` and `docs/strategies/spx-iron-fly/` |
| Session / risk                 | `src/trade_desk/engine/` |
| Desk page                      | `src/trade_desk/web/` |

New broker = new package under `brokers/` implementing `Broker`. New strategy = new package under `strategies/` implementing `Strategy`, plus `docs/strategies/<id>/`.
