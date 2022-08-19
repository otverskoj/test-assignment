from typing import Dict, Type

from src.user.repositories.core.factories_storage import IUserRepositoryFactoriesStorage
from src.user.repositories.core.repository_factory import IUserRepositoryFactory


class UserRepositoryFactoriesStorageImpl(IUserRepositoryFactoriesStorage):
    __slots__ = ('__factories',)

    def __init__(self) -> None:
        self.__factories: Dict[str, Type[IUserRepositoryFactory]] = {}
    
    def get_factory(self, repo_type: str) -> Type[IUserRepositoryFactory]:
        if repo_type in self.__factories:
            return self.__factories[repo_type]
        raise KeyError(
            f'Factory for "{repo_type}" repository is not registered'
        )

    def register(
        self, 
        fac_class: Type[IUserRepositoryFactory]
    ) -> None:
        repo_type = fac_class.repo_type()
        if repo_type in self.__factories:
            raise KeyError(
                f'Factory for "{repo_type}" repository is already registered'
            )
        self.__factories[repo_type] = fac_class

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
