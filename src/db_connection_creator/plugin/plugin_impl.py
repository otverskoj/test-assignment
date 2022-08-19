from src.db_connection_creator.core.factory import IDBConnectionCreatorFactory
from ..impl.types.postgres_connection_creator.factory_impl import PostgresConnectionCreatorFactory
from src.db_connection_creator.plugin.config import DBConnectionCreatorPluginConfig
from src.db_connection_creator.impl.factories_storage_impl import DBConnectionCreatorFactoriesStorageImpl
from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin.core.plugin import IPlugin


class DBConnectionCreatorPlugin(IPlugin):
    __slots__ = (
        '__config',
    )

    def __init__(self, config: DBConnectionCreatorPluginConfig) -> None:
        self.__config = config

    def initialize(self) -> None:
        if self.__config.type == 'none':
            return

        storage = DBConnectionCreatorFactoriesStorageImpl()
        storage.register(PostgresConnectionCreatorFactory(
            settings=self.__config.settings
        ))
        fac = storage.get_factory(self.__config.type)

        ioc.set_instance(IDBConnectionCreatorFactory, fac)

    def deinitialize(self) -> None:
        pass
