from src.entities.accounts import (
    AccountCreated,
    AccountLeadTime,
    AccountRequested,
)


def handle_account_created(
    AccountRequested: AccountRequested, AccountCreated: AccountCreated
) -> AccountLeadTime:
    return AccountLeadTime(
        AccountRequested.aggregate_id,
        (
            AccountCreated.payload.created_time
            - AccountRequested.payload.requested_time
        ),
    )
