from dataclasses import dataclass
from typing import Literal
from uuid import UUID

AggregateType: "TypeAlias" = Literal["Project"]


@dataclass
class BaseEvent:
    aggregateId: str
    aggregateType: AggregateType
    aggregateVersion: int
    eventId: UUID
    eventVersion: int
