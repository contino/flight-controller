from dataclasses import dataclass


# Base event used across all other events
@dataclass
class BaseEvent:
    aggregate_id: str
