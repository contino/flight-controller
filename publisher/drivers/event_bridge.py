import json
from typing import Dict, Any, List, Union

import boto3

from publisher.drivers.event_sink import EventSink
from publisher.entities.events import Event


class EventBridge(EventSink):
    def __init__(self) -> None:
        self.event_bridge_client = boto3.client("events")

    def _split_events(self, events: List[Dict[str, Any]]) -> Any:
        # Will split events based on eventbridge constraint for 10 at a time
        for i in range(0, len(events), 10):
            yield events[i:i + 10]

    def _format_events(self, event: Dict) -> Dict:
        return {
            "Source": "contino.flight_controller",
            "DetailType": event.event_type,
            "Detail": json.dumps(event.__dict__),
            "EventBusName": "main_lambda_bus_cdktf",
        }

    def send_events(self, events: List[Event]) -> Union[Exception, str]:
        try:
            events = [self._format_events(event) for event in events]
            if len(events) > 10:
                event_groups = self._split_events(events)
                response = []
                for event_group in event_groups:
                    response.append(self.event_bridge_client.put_events(Entries=event_group))
            else:
                response = self.event_bridge_client.put_events(Entries=events)
            return str(response)
        except Exception as err:
            return err
