# trade-desk

Private trading desk: **one engine**, pluggable **strategies**, pluggable **brokers**.

SPX 0DTE iron fly is the first product surface — a semi-manual [Captain's Log](docs/strategies/spx-iron-fly/captains-log.md) page — not the name of the platform.

## Layout

```text
docs/specs/                  engine, broker port, strategy port
docs/strategies/             per-strategy rules (iron fly first)
docs/decisions/              ADRs
src/trade_desk/domain/       quotes, chains, orders, fills
src/trade_desk/broker/       Broker protocol
src/trade_desk/brokers/      adapters (Tradier first)
src/trade_desk/strategy/     Strategy protocol
src/trade_desk/strategies/   implementations (spx_iron_fly first)
src/trade_desk/engine/       session + risk rails
src/trade_desk/web/          desk UI
tests/
```

The engine talks only to ports. `strategies/spx_iron_fly` must not import Tradier. `brokers/tradier` must not know what an iron fly is.

## Run

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[web,dev]"
cp .env.example .env
pytest
uvicorn trade_desk.web.app:app --reload
```

Then open http://127.0.0.1:8000/iron-fly

No live orders yet. The blotter is driven by a fixture so the page exists before Tradier is wired.

## Mode

| Mode      | Quotes                         | Orders                          |
|-----------|--------------------------------|---------------------------------|
| `manual`  | refresh the view model         | you place elsewhere             |
| `confirm` | refresh + compute add / close  | engine sends only after a click |
| `auto`    | same                           | engine may send (not for iron fly yet) |

Iron fly starts in **confirm**.
