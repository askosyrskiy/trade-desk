from __future__ import annotations

from typing import Any

from trade_desk.domain.models import Fill, Intent, Quote, SessionMode
from trade_desk.strategies.spx_iron_fly.view import CaptainsLog, sample_log


class SpxIronFly:
    id = "spx-iron-fly"
    display_name = "SPX 0DTE iron fly"
    underlyings = ("SPX",)
    mode = SessionMode.CONFIRM

    def __init__(self) -> None:
        self._log: CaptainsLog = sample_log()
        self._intents: list[Intent] = []

    def on_quote(self, quote: Quote) -> None:
        if quote.symbol not in self.underlyings:
            return
        self._log.last_price = quote.last

    def on_fill(self, fill: Fill) -> None:
        del fill

    def pending_intents(self) -> list[Intent]:
        return list(self._intents)

    def view_model(self) -> dict[str, Any]:
        data = self._log.as_dict()
        data["sample"] = True
        return data
