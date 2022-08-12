from abc import ABC, abstractmethod
from typing import Type

from app.storage.repositories.repository_factory import IUserRepositoryFactory


class IUserRepositoryFactoryStorage(ABC):
    @abstractmethod
    def register(
        self,
        fac: IUserRepositoryFactory
    ) -> None:
        pass

    @abstractmethod
    def unregister(
        self,
        fac_class: Type[IUserRepositoryFactory]
    ) -> None:
        pass

    @abstractmethod
    def get_factory(self, repo_type: str) -> IUserRepositoryFactory:
        pass
