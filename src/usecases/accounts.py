from typing import List, Optional
from src.entities.events import Event
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

# def handle_account_created(
#     event: AccountCreated, events: List[Event]
# ) -> Optional[AccountLeadTime]:
#     account_event = 0
#     for i, aggregate_event in enumerate(events):
#         if isinstance(aggregate_event, AccountCreated):
#             account_event = i
#     for aggregate_event in events[account_event:]:
#         if isinstance(aggregate_event, AccountRequested):
#             return AccountLeadTime(
#                 event.aggregateId,
#                 (event.payload.created_time - aggregate_event.payload.requested_time),
#             )
#     return None