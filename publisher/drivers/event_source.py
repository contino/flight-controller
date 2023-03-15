from abc import ABC, abstractmethod
from typing import Tuple, Union, Optional

from publisher.entities.events import Event


class EventSource(ABC):
    @abstractmethod
    def get_events(self, file_data: dict, repo_name: Optional[str]) -> Union[Exception, Tuple[Event]]:
        raise NotImplementedError()  # pragma: no cover
    