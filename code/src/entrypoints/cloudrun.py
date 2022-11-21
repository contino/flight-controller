import base64
import json
import os
from typing import Any, Literal, Tuple, Union

import structlog
from flask import Flask, request
from src.adapters.controller import handle_event
from src.drivers.bigquery import (
    BigQueryEventSink,
    BigQueryEventSource,
    BigQueryMetricSink,
)

app = Flask(__name__)


log = structlog.get_logger(__name__)


@app.route("/", methods=["POST"])
def index():
    return receive_event(request.get_json())  # pragma: no cover


event_sink = BigQueryEventSink()
event_source = BigQueryEventSource()
metric_sink = BigQueryMetricSink()


def receive_event(
    data: Any | None,
) -> Union[Tuple[str, Literal[400]], Tuple[Literal[""], Literal[200]]]:
    if not data:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(data, dict) or "message" not in data:
        msg = "invalid Pub/Sub data format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = data["message"]

    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
        log.msg("Received data", data=data)
        try:
            payload = json.loads(data)
            log.msg("Received payload", payload=payload)
            events = event_source.get_events_for_aggregate(payload["correlation_id"])
            log.msg("Returned aggregate events", events=events)
            response = handle_event(payload, events)
            if isinstance(response, Exception):
                log.msg("Exception handling event", exception=str(response))
            else:
                event, metrics = response
                log.msg("Received from handling event", response=str(response))
                event_sink.store_events([event])
                metric_sink.store_metrics(metrics)
            return ("", 200)
        except json.JSONDecodeError:
            msg = "Payload not in JSON format"
            return f"Bad Request: {msg}", 400
    else:
        msg = "Invalid message format"
        return f"Bad Request: {msg}", 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))  # pragma: no cover
