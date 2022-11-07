from dateutil import parser

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
        (parser.parse(project_created.payload.created_time) - parser.parse(project_requested.payload.requested_time)).total_seconds(),
    )
