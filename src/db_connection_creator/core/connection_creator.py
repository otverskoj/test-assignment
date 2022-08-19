from abc import ABC, abstractmethod
from typing import Any


class IDBConnectionCreator(ABC):
    @classmethod
    @abstractmethod
    def type(cls):
        pass

    @abstractmethod
    def get_connection(self) -> Any:
        pass
