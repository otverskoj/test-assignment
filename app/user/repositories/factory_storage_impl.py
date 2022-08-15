from typing import Dict, Type

from .factory_storage import IUserRepositoryFactoryStorage
from .repository_factory import IUserRepositoryFactory


class UserRepositoryFactoryStorageImpl(IUserRepositoryFactoryStorage):
    __slots__ = ('__factories',)

    def __init__(self) -> None:
        self.__factories: Dict[str, IUserRepositoryFactory] = {}
    
    def get_factory(self, repo_type: str) -> IUserRepositoryFactory:
        if repo_type in self.__factories:
            return self.__factories[repo_type]
        raise KeyError(
            f'Factory for "{repo_type}" repository is not registered'
        )

    def register(
        self, 
        fac: IUserRepositoryFactory
    ) -> None:
        repo_type = fac.repo_type()
        if repo_type in self.__factories:
            raise KeyError(
                f'Factory for "{repo_type}" repository is already registered'
            )
        self.__factories[repo_type] = fac

    def unregister(
        self,
        fac_class: Type[IUserRepositoryFactory]
    ) -> None:
        repo_type = fac_class.repo_type()
        if repo_type not in self.__factories:
            raise KeyError(
                f'Factory for "{repo_type}" repository is not registered'
            )
        del self.__factories[repo_type]
