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

non_compliant_aggregate_event = ResourceFoundNonCompliant(
    aggregate_id=str(uuid4()),
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=ResourceFoundNonCompliantPayload(
        container_id=str(uuid4()), timestamp=int(time())
    ),
)

non_compliant_event = ResourceFoundNonCompliant(
    aggregate_id=non_compliant_aggregate_event.aggregate_id,
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=ResourceFoundNonCompliantPayload(
        container_id=non_compliant_aggregate_event.payload.container_id, timestamp=int(time())
    ),
)

compliant_event = ResourceFoundCompliant(
    aggregate_id=non_compliant_aggregate_event.aggregate_id,
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=ResourceFoundNonCompliantPayload(
        container_id=non_compliant_aggregate_event.payload.container_id, timestamp=int(non_compliant_aggregate_event.payload.timestamp + 10)
    ),
)


def test_resource_found_non_compliant_returns_correct_event_type():
    assert isinstance(
        handle_resource_found_non_compliant(non_compliant_event, [])[0],
        ResourceFoundNonCompliant,
    )


def test_resource_found_compliant_returns_with_no_history_returns_correct_event_type():
    assert isinstance(
        handle_resource_found_compliant(compliant_event, [])[0], ResourceFoundCompliant
    )


def test_resource_found_compliant_returns_with_no_history_returns_no_metric():
    assert len(handle_resource_found_compliant(compliant_event, [])[1]) == 0


def test_resource_found_compliant_returns_with_history_returns_compliance_lead_time():
    compliant_event.aggregate_version = 2
    assert isinstance(
        handle_resource_found_compliant(
            compliant_event, [non_compliant_aggregate_event]
        )[1][0],
        ResourceComplianceLeadTime,
    )


def test_resource_found_compliant_returns_with_history_returns_correct_lead_time():
    compliant_event.aggregate_version = 2
    assert (
        handle_resource_found_compliant(
            compliant_event, [non_compliant_aggregate_event]
        )[1][0].metric_value
        == 10
    )


def test_resource_found_compliant_returns_with_multiple_history_events_returns_correct_lead_time():
    second_non_compliant_aggregate_event = ResourceFoundNonCompliant(
        aggregate_id=non_compliant_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="resource_found_non_compliant",
        aggregate_version=2,
        payload=ResourceFoundNonCompliantPayload(
            container_id=non_compliant_aggregate_event.payload.container_id,
            timestamp=int(non_compliant_aggregate_event.payload.timestamp + 5),
        ),
    )
    compliant_event.aggregate_version = 3
    assert (
        handle_resource_found_compliant(
            compliant_event,
            [non_compliant_aggregate_event, second_non_compliant_aggregate_event],
        )[1][0].metric_value
        == 10
    )


def test_resource_found_compliant_returns_correct_lead_time_from_oldest_pertinent_non_compliant():
    second_compliant_aggregate_event = ResourceFoundCompliant(
        aggregate_id=non_compliant_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="resource_found_compliant",
        aggregate_version=2,
        payload=ResourceFoundCompliantPayload(
            container_id=non_compliant_aggregate_event.payload.container_id,
            timestamp=int(non_compliant_aggregate_event.payload.timestamp + 4),
        ),
    )
    third_non_compliant_aggregate_event = ResourceFoundNonCompliant(
        aggregate_id=non_compliant_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="resource_found_non_compliant",
        aggregate_version=3,
        payload=ResourceFoundNonCompliantPayload(
            container_id=non_compliant_aggregate_event.payload.container_id,
            timestamp=int(non_compliant_aggregate_event.payload.timestamp + 5),
        ),
    )
    compliant_event.aggregate_version = 4
    assert (
        handle_resource_found_compliant(
            compliant_event,
            [
                non_compliant_aggregate_event,
                second_compliant_aggregate_event,
                third_non_compliant_aggregate_event,
            ],
        )[1][0].metric_value
        == 5
    )
