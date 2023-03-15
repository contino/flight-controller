from typing import Tuple

from publisher.drivers.checkov import Checkov
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)

CHECKOV_SOURCE = Checkov()
REPO_NAME = "Flight-Controller"
FILE_DATA = {
    "check_type": "terraform",
    "results": {
        "passed_checks": [
            {
                "check_id": "CKV_AWS_88",
                "bc_check_id": "BC_AWS_PUBLIC_12",
                "check_name": "EC2 instance should not have public IP.",
                "check_result": {
                    "result": "PASSED",
                    "evaluated_keys": [
                        "associate_public_ip_address"
                    ]
                },
                "code_block": [
                    [
                        1,
                        "resource \"aws_instance\" \"web\" {\n"
                    ],
                    [
                        2,
                        "  instance_type = \"t2.micro\"\n"
                    ],
                    [
                        3,
                        "  ami           = \"ami-09b4b74c\"\n"
                    ],
                    [
                        4,
                        "}\n"
                    ]
                ],
                "file_path": "/main.tf",
                "file_abs_path": "folder/main.tf",
                "repo_file_path": "/main.tf",
                "file_line_range": [
                    1,
                    4
                ],
                "resource": "aws_instance.web",
                "evaluations": None,
                "check_class": "checkov.terraform.checks.resource.aws.EC2PublicIP",
                "fixed_definition": None,
                "entity_tags": None,
                "caller_file_path": None,
                "caller_file_line_range": None,
                "resource_address": None,
                "severity": None,
                "bc_category": None,
                "benchmarks": None,
                "description": None,
                "short_description": None,
                "vulnerability_details": None,
                "connected_node": None,
                "guideline": "https://docs.bridgecrew.io/docs/public_12",
                "details": [],
                "check_len": None,
                "definition_context_file_path": "folder/main.tf"
            },
        ],
        "failed_checks": [
            {
                "check_id": "CKV_AWS_79",
                "bc_check_id": "BC_AWS_GENERAL_31",
                "check_name": "Ensure Instance Metadata Service Version 1 is not enabled",
                "check_result": {
                    "result": "FAILED",
                    "evaluated_keys": [
                        "metadata_options/[0]/http_tokens",
                        "metadata_options/[0]/http_endpoint"
                    ]
                },
                "code_block": [
                    [
                        1,
                        "resource \"aws_instance\" \"web\" {\n"
                    ],
                    [
                        2,
                        "  instance_type = \"t2.micro\"\n"
                    ],
                    [
                        3,
                        "  ami           = \"ami-09b4b74c\"\n"
                    ],
                    [
                        4,
                        "}\n"
                    ]
                ],
                "file_path": "/main.tf",
                "file_abs_path": "folder/main.tf",
                "repo_file_path": "/main.tf",
                "file_line_range": [
                    1,
                    4
                ],
                "resource": "aws_instance.web",
                "evaluations": None,
                "check_class": "checkov.terraform.checks.resource.aws.IMDSv1Disabled",
                "fixed_definition": None,
                "entity_tags": None,
                "caller_file_path": None,
                "caller_file_line_range": None,
                "resource_address": None,
                "severity": None,
                "bc_category": None,
                "benchmarks": None,
                "description": None,
                "short_description": None,
                "vulnerability_details": None,
                "connected_node": None,
                "guideline": "https://docs.bridgecrew.io/docs/bc_aws_general_31",
                "details": [],
                "check_len": None,
                "definition_context_file_path": "folder/main.tf"
            },
        ],
        "skipped_checks": [],
        "parsing_errors": []
    },
    "summary": {
        "passed": 2,
        "failed": 10,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 5,
        "checkov_version": "2.3.45"
    },
    "url": "Add an api key '--bc-api-key <api-key>' to see more detailed insights via https://bridgecrew.cloud"
}
NO_RESULTS_FILE_DATA = {
    "name": "no_results.json"
}


def test_checkov_returns_correct_type():
    assert isinstance(CHECKOV_SOURCE.get_events(FILE_DATA, REPO_NAME), Tuple)


def test_checkov_returns_guardrail_passedtype():
    assert isinstance(CHECKOV_SOURCE.get_events(FILE_DATA, REPO_NAME)[0], GuardrailPassed)


def test_checkov_returns_guardrail_activated_type():
    assert isinstance(CHECKOV_SOURCE.get_events(FILE_DATA, REPO_NAME)[1], GuardrailActivated)


def test_checkov_returns_exception_on_no_results_file():
    assert isinstance(CHECKOV_SOURCE.get_events(NO_RESULTS_FILE_DATA, REPO_NAME), Exception)
