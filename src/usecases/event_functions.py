from src.usecases.accounts import handle_account_created, handle_account_requested
from src.usecases.compliance import (
    handle_resource_found_compliant,
    handle_resource_found_non_compliant,
)
from src.usecases.guardrail import handle_guardrail_activated, handle_guardrail_passed
from src.usecases.identity import handle_identity_created, handle_identity_requested
from src.usecases.patch import handle_patch_summary
from src.usecases.projects import (
    handle_project_assigned,
    handle_project_created,
    handle_project_requested,
)

EVENT_FUNCTIONS = {
    "account_created": handle_account_created,
    "account_requested": handle_account_requested,
    "resource_found_compliant": handle_resource_found_compliant,
    "resource_found_non_compliant": handle_resource_found_non_compliant,
    "guardrail_activated": handle_guardrail_activated,
    "guardrail_passed": handle_guardrail_passed,
    "patch_run_summary": handle_patch_summary,
    "project_assigned": handle_project_assigned,
    "project_created": handle_project_created,
    "project_requested": handle_project_requested,
    "identity_created": handle_identity_created,
    "identity_requested": handle_identity_requested,
}
