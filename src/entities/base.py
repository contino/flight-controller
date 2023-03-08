from uuid import UUID

from pydantic import BaseModel


class BaseEvent(BaseModel):
    aggregate_id: str
    aggregate_type: str
    aggregate_version: int
    event_id: UUID
    event_version: int


class BaseMetric(BaseModel):
    aggregate_id: str
    metric_value: float
