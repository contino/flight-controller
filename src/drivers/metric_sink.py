from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.metrics import Metric


class MetricSink(ABC):
    @abstractmethod
    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        raise NotImplementedError()  # pragma: no cover
