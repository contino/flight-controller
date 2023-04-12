from typing import Literal

from pydantic import BaseModel

from src.entities.base import BaseEvent, BaseMetric


class AccountRequestedPayload(BaseModel):
    timestamp: float


class AccountRequested(BaseEvent):
    aggregate_type: Literal["Account"] = "Account"
    event_version: Literal[1] = 1
    payload: AccountRequestedPayload
    event_type: Literal["account_requested"] = "account_requested"


class AccountCreatedPayload(BaseModel):
    timestamp: float


class AccountCreated(BaseEvent):
    aggregate_type: Literal["Account"] = "Account"
    event_version: Literal[1] = 1
    payload: AccountCreatedPayload
    event_type: Literal["account_created"] = "account_created"


class AccountLeadTime(BaseMetric):
    metric_type: Literal["account_lead_time"] = "account_lead_time"
