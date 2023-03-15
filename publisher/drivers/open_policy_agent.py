from time import time
from typing import Tuple, Union

from publisher.drivers.event_source import EventSource
from publisher.entities.events import (
    Event,
    GuardrailActivated,
    GuardrailPassed,
)


class OpenPolicyAgent(EventSource):
    def get_events(self, file_data: dict, repo_name: str) -> Union[Exception, Tuple[Event]]:
        current_time = int(time())
        events = []
        if "results" in file_data:
            for result in file_data["results"]:
                if result["allow"] == True:
                    events.append(GuardrailPassed(
                        aggregate_id = repo_name + "." + result["input"]["metadata"]["namespace"] + "."  + result["input"]["metadata"]["name"],
                        guardrail_id = result["query"],
                        time = current_time,
                    ))
                else:
                    events.append(GuardrailActivated(
                        aggregate_id = repo_name + "." + result["input"]["metadata"]["namespace"] + "." + result["input"]["metadata"]["name"],
                        guardrail_id = result["query"],
                        time = current_time,
                    ))
            return tuple(events)
        return Exception(f"Unable to read Open Policy Agent results from file")
