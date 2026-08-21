"""Session wires a Strategy to a Broker. It does not know Tradier or iron flies by name."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from trade_desk.broker.port import Broker
from trade_desk.domain.models import Intent, SessionMode
from trade_desk.strategy.port import Strategy


@dataclass
class RiskPolicy:
    max_concurrent_flies: int = 6
    flatten_on_disconnect: bool = True


class Session:
    def __init__(
        self,
        strategy: Strategy,
        broker: Broker,
        risk: RiskPolicy | None = None,
        mode: SessionMode | None = None,
    ) -> None:
        self.strategy = strategy
        self.broker = broker
        self.risk = risk or RiskPolicy()
        self.mode = mode or strategy.mode

    def refresh_underlying(self, symbol: str) -> None:
        quote = self.broker.get_quote(symbol)
        self.strategy.on_quote(quote)

    def pending_intents(self) -> list[Intent]:
        return self.strategy.pending_intents()

    def view_model(self) -> dict[str, Any]:
        model = self.strategy.view_model()
        model["mode"] = self.mode.value
        model["broker"] = self.broker.id
        model["strategy"] = self.strategy.id
        return model

    def confirm(self, intent: Intent) -> None:
        if self.mode == SessionMode.MANUAL:
            raise RuntimeError("manual mode does not send orders")
        del intent
        raise NotImplementedError("order routing not wired yet")
