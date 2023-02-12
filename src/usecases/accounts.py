from src.entities.accounts import (
    AccountCreated,
    AccountAssigned,
    AccountRequested,
    AccountAssignedLeadTime,
    AccountLeadTime,
)

def handle_account_assigned(
    account_requested: AccountRequested, account_assigned: AccountAssigned
) -> AccountAssignedLeadTime:
    return AccountAssignedLeadTime(
        account_requested.aggregateId,
        account_requested.payload.account_id,
        (account_assigned.payload.assigned_time - account_requested.payload.requested_time),
    )


def handle_account_created(
    account_requested: AccountRequested, account_created: AccountCreated
) -> AccountLeadTime:
    return AccountLeadTime(
        account_requested.aggregateId,
        account_requested.payload.account_id,
        (account_created.payload.created_time - account_requested.payload.requested_time),
    )
