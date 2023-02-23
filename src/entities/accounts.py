from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent
from .base import BaseMetric


@dataclass
class AccountRequestedPayload:
    account_id: str
    requested_time: float


@dataclass
class AccountRequested(BaseEvent):
    payload: AccountRequestedPayload
    eventType: Literal["AccountRequested"] = "AccountRequested"


@dataclass
class AccountCreatedPayload:
    account_id: str
    created_time: float


@dataclass
class AccountCreated(BaseEvent):
    payload: AccountCreatedPayload
    eventType: Literal["AccountCreated"] = "AccountCreated"


@dataclass
class AccountLeadTime(BaseMetric):
    lead_time: float
    metricType: Literal["AccountLeadTime"] = "AccountLeadTime"
