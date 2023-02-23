from src.entities.projects import (
    ProjectCreated,
    ProjectLeadTime,
    ProjectRequested,
)


def handle_project_created(
    ProjectRequested: ProjectRequested, ProjectCreated: ProjectCreated
) -> ProjectLeadTime:
    return ProjectLeadTime(
        ProjectRequested.payload.project_id,
        (ProjectCreated.payload.created_time - ProjectRequested.payload.requested_time),
    )
