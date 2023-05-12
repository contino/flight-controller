from uuid import UUID

from pydantic import BaseModel


class BaseEvent(BaseModel):
    aggregate_id: str
    aggregate_type: str
    aggregate_version: int
    event_id: UUID
    event_version: int

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.dict(by_alias=True) == other.dict(by_alias=True)
        return NotImplemented


class BaseMetric(BaseModel):
    aggregate_id: str
    metric_value: float

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.dict(by_alias=True) == other.dict(by_alias=True)
        return NotImplemented
