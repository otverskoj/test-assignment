from abc import ABC, abstractmethod

from src.db_connection_creator.core.connection_creator import IDBConnectionCreator


class IDBConnectionCreatorFactory(ABC):
    __slots__ = ()

    @classmethod
    @abstractmethod
    def type(cls):
        pass

    @abstractmethod
    def get_connection_creator(self) -> IDBConnectionCreator:
        pass
