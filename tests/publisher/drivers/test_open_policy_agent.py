from typing import Tuple

from publisher.drivers.open_policy_agent import OpenPolicyAgent
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)

OPA_SOURCE = OpenPolicyAgent()
REPO_NAME = "Flight-Controller"
FILE_DATA = {
    "results": [
        {
            "allow": True,
            "query": "data.kubernetes.admission.allow",
            "timestamp": "2023-03-03T10:00:00Z",
            "input": {
                "kind": {
                    "kind": "Pod",
                    "apiVersion": "v1"
                },
                "metadata": {
                    "name": "example-pod",
                    "namespace": "example-namespace",
                    "creationTimestamp": "2023-03-03T10:00:00Z",
                    "labels": {
                        "app": "example-app"
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": "example-container",
                            "image": "example-image",
                            "ports": [
                                {
                                    "containerPort": 80
                                }
                            ]
                        }
                    ]
                }
            }
        },
        {
            "allow": False,
            "query": "data.kubernetes.admission.deny",
            "timestamp": "2023-03-03T10:01:00Z",
            "input": {
                "kind": {
                    "kind": "Pod",
                    "apiVersion": "v1"
                },
                "metadata": {
                    "name": "restricted-pod",
                    "namespace": "restricted-namespace",
                    "creationTimestamp": "2023-03-03T10:01:00Z",
                    "labels": {
                        "app": "restricted-app"
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": "restricted-container",
                            "image": "restricted-image",
                            "ports": [
                                {
                                    "containerPort": 8080
                                }
                            ]
                        }
                    ]
                }
            },
            "message": "Pod creation denied by policy"
        }
    ]
}
NO_RESULTS_FILE_DATA = {
    "name": "no_results.json"
}


def test_open_policy_agent_returns_correct_type():
    assert isinstance(OPA_SOURCE.get_events(FILE_DATA, REPO_NAME), Tuple)


def test_open_policy_agent_returns_guardrail_passedtype():
    assert isinstance(OPA_SOURCE.get_events(FILE_DATA, REPO_NAME)[0], GuardrailPassed)


def test_open_policy_agent_returns_guardrail_activated_type():
    assert isinstance(OPA_SOURCE.get_events(FILE_DATA, REPO_NAME)[1], GuardrailActivated)


def test_open_policy_agent_returns_exception_on_empty_file():
    assert isinstance(OPA_SOURCE.get_events(NO_RESULTS_FILE_DATA, REPO_NAME), Exception)
