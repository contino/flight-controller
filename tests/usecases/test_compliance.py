from time import time
from uuid import uuid4


from src.entities.compliance import (
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.usecases.compliance import (
    handle_resource_found_compliant,
    handle_resource_found_non_compliant,
)

event = ResourceFoundNonCompliant(
    uuid4(),
    "Resource",
    1,
    uuid4(),
    1,
    ResourceFoundNonCompliantPayload(container_id=uuid4(), timestamp=int(time())),
)

compliant_event = ResourceFoundCompliant(
    event.aggregate_id,
    "Resource",
    2,
    uuid4(),
    1,
    ResourceFoundCompliantPayload(
        container_id=uuid4(), timestamp=(event.payload.timestamp + 10)
    ),
)


def test_resource_found_non_compliant_returns_none():
    assert handle_resource_found_non_compliant(event, []) is None


def test_resource_found_compliant_returns_with_no_history_returns_none():
    assert handle_resource_found_compliant(event, []) is None


def test_resource_found_compliant_returns_with_history_returns_compliance_lead_time():
    assert isinstance(
        handle_resource_found_compliant(compliant_event, [event]),
        ResourceComplianceLeadTime,
    )


def test_resource_found_compliant_returns_with_history_returns_correct_lead_time():
    assert handle_resource_found_compliant(compliant_event, [event]).lead_time == 10


def test_resource_found_compliant_returns_with_multiple_history_events_returns_correct_lead_time():
    second_event = ResourceFoundNonCompliant(
        event.aggregate_id,
        "Resource",
        2,
        uuid4(),
        1,
        ResourceFoundNonCompliantPayload(
            container_id=uuid4(), timestamp=(event.payload.timestamp + 5)
        ),
    )
    assert (
        handle_resource_found_compliant(
            compliant_event, [event, second_event]
        ).lead_time
        == 10
    )


def test_resource_found_compliant_returns_correct_lead_time_from_oldest_pertinent_non_compliant():
    second_event = ResourceFoundCompliant(
        event.aggregate_id,
        "Resource",
        2,
        uuid4(),
        1,
        ResourceFoundCompliantPayload(
            container_id=uuid4(), timestamp=(event.payload.timestamp + 4)
        ),
    )
    third_event = ResourceFoundNonCompliant(
        event.aggregate_id,
        "Resource",
        2,
        uuid4(),
        1,
        ResourceFoundNonCompliantPayload(
            container_id=uuid4(), timestamp=(event.payload.timestamp + 5)
        ),
    )
    assert (
        handle_resource_found_compliant(
            compliant_event, [event, second_event, third_event]
        ).lead_time
        == 5
    )
