from typing import Dict, Type

from app.storage.repositories.factory_storage import IUserRepositoryFactoryStorage
from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.errors.factory_not_registered import FactoryNotRegistered


class UserRepositoryFactoryStorageImpl(IUserRepositoryFactoryStorage):
    __slots__ = ('__factories',)

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(UserRepositoryFactoryStorageImpl, cls).__new__(cls)
    #     return cls.instance

    def __init__(self) -> None:
        self.__factories: Dict[str, IUserRepositoryFactory] = {}
    
    def get_factory(self, repo_type: str) -> IUserRepositoryFactory:
        if repo_type in self.__factories:
            return self.__factories[repo_type]
        raise FactoryNotRegistered(
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
