from dataclasses import dataclass
from typing import Literal

# Base event used across all other events
@dataclass
class BaseEvent:
    detail_type: str
