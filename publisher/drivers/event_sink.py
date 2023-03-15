from abc import ABC, abstractmethod
from typing import List, Optional, Union

from publisher.entities.events import Event


class EventSink(ABC):
    @abstractmethod
    def send_events(self, events: List[Event]) -> Union[Exception, str]:
        raise NotImplementedError()  # pragma: no cover
