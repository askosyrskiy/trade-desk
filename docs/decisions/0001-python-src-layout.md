# 0001 — Python src layout

Date: 2026-08-20

## Decision

`trade-desk` is a single Python package (`src/trade_desk`) with ports under `broker/` and `strategy/`, adapters under `brokers/`, implementations under `strategies/`, and a FastAPI desk under `web/`.

## Why

Existing local trading work (Tradier, other agents) is Python. The GitHub `.gitignore` on the empty repo was the Python template. A JS monorepo would fight that. Split packages can wait until a second broker ships.

## Consequences

- Install with `pip install -e ".[web,dev]"`
- Composition root is `trade_desk.web.app` (and later a worker)
- UI is this app, not Umbraco, until we deliberately embed it
