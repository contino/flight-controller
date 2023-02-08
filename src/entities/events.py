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

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload
)

Event: "TypeAlias" = Union[ProjectCreated, ProjectRequested, AccountCreated, AccountRequested, ResourceFoundNonCompliant]

EventType: "TypeAlias" = Union[
    
    Literal["ProjectCreated"],
   
    Literal["ProjectRequested"],
    Literal["AccountCreated"],
    Literal["AccountRequested"]
    ,
    Literal["ResourceFoundNonCompliant"],
]

Payload: "TypeAlias" = Union[
    ProjectCreatedPayload, ProjectRequestedPayload, AccountCreatedPayload, AccountRequestedPayload, ResourceFoundNonCompliantPayload
]
