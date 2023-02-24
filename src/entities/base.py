from dataclasses import dataclass
from typing import Literal, Union
from uuid import UUID

aggregate_type: "TypeAlias" = Union[Literal["Project"], Literal["Resource"], Literal["Account"]]


@dataclass
class BaseEvent:
    aggregate_id: str
    aggregate_type: aggregate_type
    aggregate_version: int
    event_id: UUID
    event_version: int


@dataclass
class BaseMetric:
    aggregate_id: str
