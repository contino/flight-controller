from time import time
from uuid import uuid4

from src.entities.patch import (
    PatchCompliancePercentage,
    PatchRunSummary,
    PatchRunSummaryPayload
)
from src.usecases.patch import (
    handle_patch_summary,
)

event = PatchRunSummary(
    uuid4(),
    "Account",
    1,
    uuid4(),
    1,
    PatchRunSummaryPayload(failed_instances="i-adslkjfds,i-89dsfkjdkfj", successful_instances="i-peoritdsfl"),
)


def test_patch_summary_returns_patch_compliance_percentage():
    assert isinstance(
        handle_patch_summary(event),
        PatchCompliancePercentage,
    )


def test_patch_summary_returns_correct_patch_compliance_percentage():
    assert handle_patch_summary(event).percentage == 33.3
