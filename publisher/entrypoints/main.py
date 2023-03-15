import argparse

import structlog

from publisher.drivers.file_source import FileSource
from publisher.drivers.git import Git
from publisher.drivers.sink import SINK
from publisher.drivers.source import SOURCE

file_source = FileSource()
git = Git()
logger = structlog.get_logger(__name__)


def main(args: argparse.Namespace):
    if not args.source or not args.file or not args.sink:
        logger.error("One or more arguments (sink, file and source) are missing")
        return Exception("One or more arguments (sink, file and source) are missing")
    
    file_data = file_source.read_file(args.file)
    if isinstance(file_data, Exception):
        logger.error(f"Exception from file source while reading file: {args.file}", exception=str(file_data))
        return file_data
    
    repo_name = git.get_repo_name()
    if isinstance(repo_name, Exception):
        logger.error(f"Exception from git while retrieving repository name.", exception=str(repo_name))
        return repo_name 

    if args.source in SOURCE:
        response = SOURCE[args.source]().get_events(file_data, repo_name)
        if isinstance(response, Exception):
            logger.error(f"Exception from {args.source} event source", exception=str(response))
            return response
        events = response
        logger.msg(f"Received from {args.source} event source", response=str(response))
        
        if args.sink in SINK:
            response = SINK[args.sink]().send_events(events)
            if isinstance(response, Exception):
                logger.error(f"Exception from {args.sink} event sink", exception=str(response))
                return response
            logger.msg(f"Received from {args.sink} event sink", response=str(response))
            return response

        logger.error(f"{args.sink} is not a supported event sink")
        return Exception(f"{args.sink} is not a supported event sink")

    logger.error(f"{args.source} is not a supported event source")
    return Exception(f"{args.source} is not a supported event source")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The custom event producer for Flight Controller.", epilog="Additional text for the help page") # pragma: no cover
    parser.add_argument("-so", "--source", type=str, choices=SOURCE, help="The source in which you want to get events from.", required=True) # pragma: no cover
    parser.add_argument("-f", "--file", type=str, help="The json file in which to parse result into events.", required=True) # pragma: no cover
    parser.add_argument("-si", "--sink", type=str, choices=SINK, help="The sink in which you want to send events to.", required=True) # pragma: no cover
    args = parser.parse_args() # pragma: no cover

    main(args) # pragma: no cover
    