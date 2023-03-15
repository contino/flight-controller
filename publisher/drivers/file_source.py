import json
from typing import Dict, Union


class FileSource():
    def read_file(self, file: str) -> Union[Exception, Dict]:
        try:
            with open(file, "r") as file:
                return json.loads(file.read())
        except FileNotFoundError as err:
            return err
        except Exception as err:
            return err
