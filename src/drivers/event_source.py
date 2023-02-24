from abc import ABC, abstractmethod
from typing import List, Union

from src.entities.events import Event


class EventSource(ABC):
    @abstractmethod
    def get_events_for_aggregate(
        self, aggregate_id: str
    ) -> Union[Exception, List[Event]]:
        raise NotImplementedError()  # pragma: no cover
