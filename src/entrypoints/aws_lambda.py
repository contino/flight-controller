import structlog

from src.adapters.controller import handle_event
from src.drivers.dynamo_event_sink_source import DynamoEventSink, DynamoEventSource
from src.drivers.timestream_metric_sink import TimeStreamMetricSink


logger = structlog.get_logger(__name__)
event_source = DynamoEventSource()
event_sink = DynamoEventSink()
metric_sink = TimeStreamMetricSink()


def lambda_handler(event, _) -> None:
    logger.msg("Incoming event", incoming_event=event)
    full_event = event["detail"]
    aggregate_events = event_source.get_events_for_aggregate(full_event["aggregate_id"])
    if isinstance(aggregate_events, Exception):
            logger.error("Exception retrieving aggregate events", exception=str(aggregate_events))
    logger.msg("Aggregate event/s retrieved", aggregate_count=len(aggregate_events))
    response = handle_event(full_event, aggregate_events)
    if isinstance(response, Exception):
        logger.error("Exception handling event", exception=str(response))
    else:
        event, metrics = response
        logger.msg("Received from handling event", outgoing_event=str(event), outgoing_metrics=str(metrics))
        response = event_sink.store_events([event])
        if isinstance(response, Exception):
            logger.error("Exception storing event", exception=str(response))
        logger.info("Event stored in DynamoDB", stored_event=str(event))
        response = metric_sink.store_metrics(metrics)
        if isinstance(response, Exception):
            logger.error("Exception storing metric", exception=str(response))
        logger.info("Metrics stored in Timestream", stored_metrics=str(metrics))

