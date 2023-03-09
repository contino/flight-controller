import json
from typing import Dict

import structlog

LOGGER = structlog.get_logger(__name__)


class FileSource():
    def read_file(self, file: str) -> Dict:
        try:
            with open(file, "r") as file:
                return json.loads(file.read())
        except FileNotFoundError as err:
            LOGGER.error(f"File {file} not found!", exception=str(err))
            return err
        except Exception as err:
            LOGGER.error(f"file_source.py raised an exception", exception=str(err))
            return err

