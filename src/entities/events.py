from typing import Literal, Union

from src.entities.compliance import (
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)

from .projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)

Event: "TypeAlias" = Union[ProjectCreated, ProjectRequested, ResourceFoundNonCompliant]

EventType: "TypeAlias" = Union[
    Literal["ProjectCreated"],
    Literal["ProjectRequested"],
    Literal["ResourceFoundNonCompliant"],
]

Payload: "TypeAlias" = Union[
    ProjectCreatedPayload, ProjectRequestedPayload, ResourceFoundNonCompliantPayload
]
