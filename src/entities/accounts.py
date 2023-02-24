from dataclasses import dataclass
from typing import Literal

from src.entities.base import BaseEvent, BaseMetric


@dataclass
class AccountRequestedPayload:
    account_id: str
    requested_time: float


@dataclass
class AccountRequested(BaseEvent):
    payload: AccountRequestedPayload
    event_type: Literal["account_requested"] = "account_requested"


@dataclass
class AccountCreatedPayload:
    account_id: str
    created_time: float


@dataclass
class AccountCreated(BaseEvent):
    payload: AccountCreatedPayload
    event_type: Literal["account_created"] = "account_created"


@dataclass
class AccountLeadTime(BaseMetric):
    lead_time: float
    metric_type: Literal["account_lead_time"] = "account_lead_time"
