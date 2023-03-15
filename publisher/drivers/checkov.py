from time import time
from typing import Tuple, Union

from publisher.drivers.event_source import EventSource
from publisher.entities.events import (
    Event,
    GuardrailActivated,
    GuardrailPassed,
)


class Checkov(EventSource):    
    def get_events(self, file_data: dict, repo_name: str) -> Union[Exception, Tuple[Event]]:
        current_time = int(time())
        events = []
        if "results" in file_data:
            for result in file_data["results"]["passed_checks"]:
                events.append(GuardrailPassed(
                    aggregate_id = repo_name + "." + result["resource"],
                    guardrail_id = result["check_id"],
                    time = current_time,
                ))
            for result in file_data["results"]["failed_checks"]:
                events.append(GuardrailActivated(
                    aggregate_id = repo_name + "." + result["resource"],
                    guardrail_id = result["check_id"],
                    time = current_time,
                ))
            return tuple(events)
        return Exception(f"Unable to read Checkov results from file")
        