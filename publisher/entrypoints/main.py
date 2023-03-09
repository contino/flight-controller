import argparse

import structlog

from publisher.drivers.event_bridge import EventBridge
from publisher.drivers.sink import SINK
from publisher.drivers.source import SOURCE

LOGGER = structlog.get_logger(__name__)
EVENT_BRIDGE = EventBridge()


def main(args: argparse.Namespace):
    if not args.source or not args.file or not args.sink:
        return Exception("Arguments sink, file and source are missing")
    if args.source in SOURCE:
        response = SOURCE[args.source]().get_events(args.file)
        if isinstance(response, Exception):
            LOGGER.error(f"Exception from {args.source} event source", exception=str(response))
            return response
        else:
            events = response
            LOGGER.msg(f"Received from {args.source} event source", response=str(response))
            if args.sink in SINK:
                response = SINK[args.sink]().send_events(events)
                if isinstance(response, Exception):
                    LOGGER.error(f"Exception from {args.sink} event sink", exception=str(response))
                    return response
                else:
                    LOGGER.msg(f"Received from {args.sink} event sink", response=str(response))
            else:
                LOGGER.error(f"{args.sink} is not a supported event sink")
                return Exception(f"{args.sink} is not a supported event sink")
    else:
        LOGGER.error(f"{args.source} is not a supported event source")
        return Exception(f"{args.source} is not a supported event source")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The custom event producer for Flight Controller.", epilog="Additional text for the help page") # pragma: no cover
    parser.add_argument("-so", "--source", type=str, choices=SOURCE, help="The source in which you want to get events from.", required=True) # pragma: no cover
    parser.add_argument("-f", "--file", type=str, help="The json file in which to parse result into events.", required=True) # pragma: no cover
    parser.add_argument("-si", "--sink", type=str, choices=SINK, help="The sink in which you want to send events to.", required=True) # pragma: no cover
    args = parser.parse_args() # pragma: no cover

    main(args) # pragma: no cover
    