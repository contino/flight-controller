from time import time
from typing import Tuple, Union

import structlog

from publisher.drivers.event_source import EventSource
from publisher.drivers.file_source import FileSource
from publisher.entities.events import Event
from publisher.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedDetail,
    GuardrailPassed,
    GuardrailPassedDetail,
)

LOGGER = structlog.get_logger(__name__)

class OpenPolicyAgent(EventSource):
    def __init__(self) -> None:
        self.file_source = FileSource()

    def get_events(self, file: str) -> Union[Exception, Tuple[Event]]:
        current_time = int(time())
        data = self.file_source.read_file(file)
        if isinstance(data, Exception):
            LOGGER.error(f"Unable to read Open Policy Agent results file: {file}", exception=str(data))
            return data
        events = []
        if "results" in data:
            for result in data["results"]:
                if result["allow"] == True:
                    events.append(GuardrailPassed(
                        source = "contino.custom",
                        detail_type = "Open Policy Agent Guardrail Passed",
                        detail = GuardrailPassedDetail(
                            aggregate_id = result["input"]["metadata"]["name"] + "-" + result["input"]["metadata"]["namespace"],
                            guardrail_id = result["query"],
                            time = current_time,
                        )
                    ))
                else:
                    events.append(GuardrailActivated(
                        source = "contino.custom",
                        detail_type = "Open Policy Agent Guardrail Activated",
                        detail = GuardrailActivatedDetail(
                            aggregate_id = result["input"]["metadata"]["name"] + "-" + result["input"]["metadata"]["namespace"],
                            guardrail_id = result["query"],
                            time = current_time,
                        )
                    ))
            return tuple(events)
        LOGGER.error(f"Unable to read Open Policy Agent results from file: {file}")
        return Exception(f"Unable to read Open Policy Agent results from file: {file}")

