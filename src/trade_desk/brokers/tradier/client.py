"""Tradier Broker adapter. Quotes, chains, and 4-leg orders only — no strategy types."""

from __future__ import annotations

import os

from trade_desk.domain.models import MultilegOrder, OptionChain, OrderRef, Position, Quote


class TradierBroker:
    id = "tradier"

    def __init__(
        self,
        access_token: str | None = None,
        account_id: str | None = None,
        base_url: str | None = None,
    ) -> None:
        self.access_token = access_token or os.environ.get("TRADIER_ACCESS_TOKEN", "")
        self.account_id = account_id or os.environ.get("TRADIER_ACCOUNT_ID", "")
        self.base_url = (
            base_url
            or os.environ.get("TRADIER_BASE_URL")
            or "https://sandbox.tradier.com/v1"
        )

    def get_quote(self, symbol: str) -> Quote:
        raise NotImplementedError("Tradier quotes not wired yet")

    def get_expirations(self, symbol: str) -> list[str]:
        raise NotImplementedError("Tradier expirations not wired yet")

    def get_chain(self, symbol: str, expiration: str) -> OptionChain:
        raise NotImplementedError("Tradier chains not wired yet")

    def preview_multileg(self, order: MultilegOrder) -> OrderRef:
        raise NotImplementedError("Tradier preview not wired yet")

    def place_multileg(self, order: MultilegOrder) -> OrderRef:
        raise NotImplementedError("Tradier place not wired yet")

    def get_order(self, broker_order_id: str) -> OrderRef:
        raise NotImplementedError("Tradier order status not wired yet")

    def get_positions(self) -> list[Position]:
        raise NotImplementedError("Tradier positions not wired yet")
