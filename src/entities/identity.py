from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent
from .base import BaseMetric


@dataclass
class IdentityRequestedPayload:
    account_id: str
    requested_time: float


@dataclass
class IdentityRequested(BaseEvent):
    payload: IdentityRequestedPayload
    event_type: Literal["identity_requested"] = "identity_requested"


@dataclass
class IdentityCreatedPayload:
    account_id: str
    created_time: float


@dataclass
class IdentityCreated(BaseEvent):
    payload: IdentityCreatedPayload
    event_type: Literal["identity_created"] = "identity_created"


@dataclass
class IdentityLeadTime(BaseMetric):
    lead_time: float
    metric_type: Literal["IdentityLeadTime"] = "IdentityLeadTime"
