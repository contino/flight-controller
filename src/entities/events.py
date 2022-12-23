from typing import Literal, Union
from typing_extensions import TypeAlias

from .projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)

Event: TypeAlias = Union[ProjectCreated, ProjectRequested]

EventType: TypeAlias = Union[Literal["ProjectCreated"], Literal["ProjectRequested"]]

Payload: TypeAlias = Union[ProjectCreatedPayload, ProjectRequestedPayload]
