import structlog

from src.adapters.controller import handle_event
from src.drivers.dynamo_event_sink_source import DynamoEventSink, DynamoEventSource
from src.drivers.timestream_metric_sink import TimeStreamMetricSink


logger = structlog.get_logger(__name__)
event_source = DynamoEventSource()
event_sink = DynamoEventSink()
metric_sink = TimeStreamMetricSink()


def lambda_handler(event, _):
    print(f"event is {event}")
    full_event = event["detail"]
    events = event_source.get_events_for_aggregate(full_event["aggregate_id"])
    logger.msg("Returned aggregate events", events=events)
    response = handle_event(full_event, events)
    if isinstance(response, Exception):
        logger.msg("Exception handling event", exception=str(response))
    else:
        event, metrics = response
        logger.msg("Received from handling event", response=str(response))
        event_sink.store_events([event])
        metric_sink.store_metrics(metrics)
