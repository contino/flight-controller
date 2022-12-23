from typing import Literal, TypeAlias, Union

from .projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)

Event: TypeAlias = Union[ProjectCreated, ProjectRequested]

EventType: TypeAlias = Union[Literal["ProjectCreated"], Literal["ProjectRequested"]]

Payload: TypeAlias = Union[ProjectCreatedPayload, ProjectRequestedPayload]
