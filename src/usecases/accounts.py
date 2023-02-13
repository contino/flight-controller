from src.entities.accounts import (
    AccountCreated,
    AccountLeadTime,
    AccountRequested,
)


def handle_account_created(
    account_requested: AccountRequested, account_created: AccountCreated
) -> AccountLeadTime:
    return AccountLeadTime(
        account_requested.aggregateId,
        (
            account_created.payload.created_time
            - account_requested.payload.requested_time
        ),
    )
