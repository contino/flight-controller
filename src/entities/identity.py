from typing import Literal

from pydantic import BaseModel

from .base import BaseEvent
from .base import BaseMetric


class IdentityRequestedPayload(BaseModel):
    account_id: str
    timestamp: float


class IdentityRequested(BaseEvent):
    aggregate_type: Literal["Identity"] = "Identity"
    event_version: Literal[1] = 1
    payload: IdentityRequestedPayload
    event_type: Literal["identity_requested"] = "identity_requested"


class IdentityCreatedPayload(BaseModel):
    account_id: str
    timestamp: float


class IdentityCreated(BaseEvent):
    aggregate_type: Literal["Identity"] = "Identity"
    event_version: Literal[1] = 1
    payload: IdentityCreatedPayload
    event_type: Literal["identity_created"] = "identity_created"


class IdentityLeadTime(BaseMetric):
    metric_type: Literal["identity_lead_time"] = "identity_lead_time"
