from time import time
from typing import Tuple, Union
from uuid import uuid4

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


class Checkov(EventSource):
    def __init__(self) -> None:
         self.file_source = FileSource()
    
    def get_events(self, file: str) -> Union[Exception, Tuple[Event]]:
        current_time = int(time())
        data = self.file_source.read_file(file)
        if isinstance(data, Exception):
            LOGGER.error(f"Unable to read Checkov results file: {file}", exception=str(data))
            return data
        events = []
        if "results" in data:
            for result in data["results"]["passed_checks"]:
                    events.append(GuardrailPassed(
                        source = "contino.custom",
                        detail_type = "Checkov Guardrail Passed",
                        detail = GuardrailPassedDetail(
                            aggregate_id = result["resource"], # Will need a better way of getting resource id, current method is not live id
                            guardrail_id = result["check_id"],
                            time = current_time,
                        )
                    ))
            for result in data["results"]["failed_checks"]:
                events.append(GuardrailActivated(
                    source = "contino.custom",
                    detail_type = "Checkov Guardrail Activated",
                    detail = GuardrailActivatedDetail(
                        aggregate_id = result["resource"], # Will need a better way of getting resource id, current method is not live id
                        guardrail_id = result["check_id"],
                        time = current_time,
                    )
                ))
            return tuple(events)
        LOGGER.error(f"Unable to read Checkov results from file: {file}")
        return Exception(f"Unable to read Checkov results from file: {file}")
        