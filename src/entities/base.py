from dataclasses import dataclass
from typing import Literal, Union
from uuid import UUID

AggregateType: "TypeAlias" = Union[Literal["Project"], Literal["Resource"]]


@dataclass
class BaseEvent:
    aggregateId: str
    aggregateType: AggregateType
    aggregateVersion: int
    eventId: UUID
    eventVersion: int


@dataclass
class BaseMetric:
    aggregate_id: str
