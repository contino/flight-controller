from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent


@dataclass
class AccountRequestedPayload:
    account_id: str
    requested_time: float


@dataclass
class AccountRequested(BaseEvent):
    payload: AccountRequestedPayload
    eventVersion: int
    eventType: Literal["AccountRequested"] = "AccountRequested"

@dataclass
class AccountAssignedPayload:
    account_id: str
    assigned_time: float


@dataclass
class AccountAssigned(BaseEvent):
    payload: AccountAssignedPayload
    eventVersion: int
    eventType: Literal["AccountAssigned"] = "AccountAssigned"


@dataclass
class AccountCreatedPayload:
    account_id: str
    created_time: float


@dataclass
class AccountCreated(BaseEvent):
    payload: AccountCreatedPayload
    eventVersion: int
    eventType: Literal["AccountCreated"] = "AccountCreated"


@dataclass
class AccountLeadTime:
    account_id: str
    lead_time: float

@dataclass
class AccountAssignedLeadTime:
    account_id: str
    lead_time: float

