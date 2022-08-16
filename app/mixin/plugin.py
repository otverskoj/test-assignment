from abc import ABC, abstractmethod
from typing import Any, Mapping


class IPlugin(ABC):
    @abstractmethod
    def initialize(self, config: Mapping[str, Any]) -> None:
        pass

    @abstractmethod
    def deinitialize(self) -> None:
        pass
