from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.events import Event


class EventSink(ABC):
    @abstractmethod
    def store_events(self, events: List[Event]) -> Optional[Exception]:
        raise NotImplementedError()  # pragma: no cover
