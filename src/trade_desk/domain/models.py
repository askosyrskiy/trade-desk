"""Broker-agnostic types. Strategies and adapters share these, not each other."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import StrEnum
from typing import Literal


class Side(StrEnum):
    BUY_TO_OPEN = "buy_to_open"
    SELL_TO_OPEN = "sell_to_open"
    BUY_TO_CLOSE = "buy_to_close"
    SELL_TO_CLOSE = "sell_to_close"


class Right(StrEnum):
    CALL = "call"
    PUT = "put"


class SessionMode(StrEnum):
    MANUAL = "manual"
    CONFIRM = "confirm"
    AUTO = "auto"


class OrderStatus(StrEnum):
    PREVIEW = "preview"
    PENDING = "pending"
    OPEN = "open"
    PARTIAL = "partially_filled"
    FILLED = "filled"
    REJECTED = "rejected"
    CANCELED = "canceled"


class IntentKind(StrEnum):
    ADD = "add"
    CLOSE = "close"
    FLATTEN = "flatten"


@dataclass(frozen=True)
class Quote:
    symbol: str
    last: float
    bid: float | None = None
    ask: float | None = None
    ts: datetime | None = None


@dataclass(frozen=True)
class OptionContract:
    occ_symbol: str
    underlying: str
    expiration: date
    strike: float
    right: Right
    bid: float | None = None
    ask: float | None = None


@dataclass(frozen=True)
class OptionChain:
    underlying: str
    expiration: date
    contracts: tuple[OptionContract, ...] = ()


@dataclass(frozen=True)
class Leg:
    occ_symbol: str
    side: Side
    quantity: int


@dataclass(frozen=True)
class MultilegOrder:
    underlying: str
    legs: tuple[Leg, ...]
    order_type: Literal["market", "credit", "debit", "even"] = "credit"
    duration: Literal["day", "gtc"] = "day"
    price: float | None = None
    tag: str | None = None


@dataclass(frozen=True)
class OrderRef:
    broker_order_id: str
    status: OrderStatus
    filled_price: float | None = None


@dataclass(frozen=True)
class Fill:
    broker_order_id: str
    occ_symbol: str
    quantity: int
    price: float
    ts: datetime


@dataclass(frozen=True)
class Position:
    occ_symbol: str
    quantity: int
    cost: float | None = None


@dataclass(frozen=True)
class Intent:
    kind: IntentKind
    reason: str
    payload: dict[str, object] = field(default_factory=dict)
