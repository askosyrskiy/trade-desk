"""Broker port. Adapters implement this. Strategies must not import adapters."""

from __future__ import annotations

from typing import Protocol

from trade_desk.domain.models import (
    MultilegOrder,
    OptionChain,
    OrderRef,
    Position,
    Quote,
)


class Broker(Protocol):
    id: str

    def get_quote(self, symbol: str) -> Quote: ...

    def get_expirations(self, symbol: str) -> list[str]: ...

    def get_chain(self, symbol: str, expiration: str) -> OptionChain: ...

    def preview_multileg(self, order: MultilegOrder) -> OrderRef: ...

    def place_multileg(self, order: MultilegOrder) -> OrderRef: ...

    def get_order(self, broker_order_id: str) -> OrderRef: ...

    def get_positions(self) -> list[Position]: ...
