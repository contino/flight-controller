from typing import Literal, Union

from src.entities.compliance import (
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload
)
from .projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)

Event: "TypeAlias" = Union[ProjectCreated, ProjectRequested, ResourceFoundNonCompliant, PatchRunSummary]

EventType: "TypeAlias" = Union[
    Literal["ProjectCreated"],
    Literal["ProjectRequested"],
    Literal["ResourceFoundNonCompliant"],
    Literal["PatchRunSummary"]
]

Payload: "TypeAlias" = Union[
    ProjectCreatedPayload, ProjectRequestedPayload, ResourceFoundNonCompliantPayload, PatchRunSummaryPayload
]
