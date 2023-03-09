from abc import ABC, abstractmethod
from typing import Tuple, Union

from publisher.entities.events import Event


class EventSource(ABC):
    @abstractmethod
    def get_events(self, file: str) -> Union[Exception, Tuple[Event]]:
        raise NotImplementedError()  # pragma: no cover
    