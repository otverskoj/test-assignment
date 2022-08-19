from typing import Dict, Type

from src.db_connection_creator.core.factories_storage import IDBConnectionCreatorFactoriesStorage
from src.db_connection_creator.core.factory import IDBConnectionCreatorFactory


class DBConnectionCreatorFactoriesStorageImpl(IDBConnectionCreatorFactoriesStorage):
    __slots__ = ('__factories',)

    def __init__(self) -> None:
        self.__factories: Dict[str, IDBConnectionCreatorFactory] = {}

    def get_factory(self, fac_type: str) -> IDBConnectionCreatorFactory:
        if fac_type in self.__factories:
            return self.__factories[fac_type]
        raise KeyError(
            f'Factory for "{fac_type}" is not registered'
        )

    def register(self, fac: IDBConnectionCreatorFactory) -> None:
        fac_type = fac.type()
        if fac_type in self.__factories:
            raise KeyError(
                f'Factory for "{fac_type}" is already registered'
            )
        self.__factories[fac_type] = fac

    def unregister(self, fac_class: Type[IDBConnectionCreatorFactory]) -> None:
        fac_type = fac_class.type()
        if fac_type not in self.__factories:
            raise KeyError(
                f'Factory for "{fac_type}" is not registered'
            )
        del self.__factories[fac_type]
