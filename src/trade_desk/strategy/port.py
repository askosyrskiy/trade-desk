"""Strategy port. Implementations emit intents and a view model. No broker imports."""

from __future__ import annotations

from typing import Any, Protocol

from trade_desk.domain.models import Fill, Intent, Quote, SessionMode


class Strategy(Protocol):
    id: str
    display_name: str
    underlyings: tuple[str, ...]
    mode: SessionMode

    def on_quote(self, quote: Quote) -> None: ...

    def on_fill(self, fill: Fill) -> None: ...

    def pending_intents(self) -> list[Intent]: ...

    def view_model(self) -> dict[str, Any]: ...
