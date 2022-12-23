from src.entities.projects import (
    ProjectCreated,
    ProjectLeadTime,
    ProjectRequested,
)


def handle_project_created(
    project_requested: ProjectRequested, project_created: ProjectCreated
) -> ProjectLeadTime:
    return ProjectLeadTime(
        project_requested.payload.project_id,
        (
            project_created.payload.created_time
            - project_requested.payload.requested_time
        ),
    )
