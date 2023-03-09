import json
from typing import Dict, Any, Optional, List, Union

import boto3
import structlog

from publisher.drivers.event_sink import EventSink
from publisher.entities.events import Event


LOGGER = structlog.get_logger(__name__)


class EventBridge(EventSink):
    def __init__(self) -> None:
        self.event_bridge_client = boto3.client("events")

    def _split_events(self, events: List[Dict[str, Any]]) -> Any:
        # Will split events based on eventbridge constraint for 10 at a time
        for i in range(0, len(events), 10):
            yield events[i:i + 10]

    def _format_events(self, event: Dict) -> Dict:
        return {
            "Source": event.source,
            "DetailType": event.detail_type,
            "Detail": json.dumps(event.detail.__dict__),
            "EventBusName": event.event_bus_name,
        }

    def send_events(self, events: List[Event]) -> Optional[Union[Exception, str]]:
        try:
            events = [self._format_events(event) for event in events]
            if len(events) > 10:
                event_groups = self._split_events(events)
                for event_group in event_groups:
                    response = self.event_bridge_client.put_events(Entries=event_group)
            else:
                response = self.event_bridge_client.put_events(Entries=events)
            return str(response)
        except Exception as err:
            return err
        
