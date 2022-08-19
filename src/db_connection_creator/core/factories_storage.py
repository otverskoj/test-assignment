from abc import ABC, abstractmethod
from typing import Type

from src.db_connection_creator.core.factory import IDBConnectionCreatorFactory
from src.user.repositories.core.repository_factory import IUserRepositoryFactory


class IDBConnectionCreatorFactoriesStorage(ABC):
    @abstractmethod
    def register(
        self,
        fac: IDBConnectionCreatorFactory
    ) -> None:
        pass

    @abstractmethod
    def unregister(
        self,
        fac_class: Type[IDBConnectionCreatorFactory]
    ) -> None:
        pass

    @abstractmethod
    def get_factory(self, fac_type: str) -> IDBConnectionCreatorFactory:
        pass
