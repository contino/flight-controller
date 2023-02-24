from src.entities.projects import (
    ProjectAssigned,
    ProjectAssignedLeadTime,
    ProjectCreated,
    ProjectLeadTime,
    ProjectRequested,
)

def handle_project_assigned(
    ProjectRequested: ProjectRequested, ProjectAssigned: ProjectAssigned
) -> ProjectAssignedLeadTime:
    return ProjectAssignedLeadTime(
        ProjectRequested.payload.project_id,
        (ProjectAssigned.payload.assigned_time - ProjectRequested.payload.requested_time),
    )


def handle_project_created(
    ProjectRequested: ProjectRequested, ProjectCreated: ProjectCreated
) -> ProjectLeadTime:
    return ProjectLeadTime(
        ProjectRequested.payload.project_id,
        (ProjectCreated.payload.created_time - ProjectRequested.payload.requested_time),
    )
