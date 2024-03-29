from time import time
from uuid import uuid4

from src.entities.patch import (
    PatchCompliancePercentage,
    PatchRunSummary,
    PatchRunSummaryPayload,
)
from src.usecases.patch import (
    handle_patch_summary,
)

event = PatchRunSummary(
    aggregate_id=str(uuid4()),
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=PatchRunSummaryPayload(
        timestamp=int(time()),
        failed_instances="i-adslkjfds,i-89dsfkjdkfj",
        successful_instances="i-peoritdsfl",
    ),
)


def test_patch_summary_returns_correct_event_type():
    assert isinstance(
        handle_patch_summary(event, [])[0], PatchRunSummary)


def test_patch_summary_returns_patch_compliance_percentage():
    assert isinstance(
        handle_patch_summary(event, [])[1][0], PatchCompliancePercentage)


def test_patch_summary_returns_correct_patch_compliance_percentage():
    assert handle_patch_summary(event, [])[1][0].metric_value == 33.3
