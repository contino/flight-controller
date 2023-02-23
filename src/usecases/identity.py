from src.entities.identity import (
    IdentityCreated,
    IdentityLeadTime,
    IdentityRequested,
)


def handle_identity_created(
    identity_requested: IdentityRequested, identity_created: IdentityCreated
) -> IdentityLeadTime:
    return IdentityLeadTime(
        identity_requested.aggregate_id,
        (
            identity_created.payload.created_time
            - identity_requested.payload.requested_time
        ),
    )
