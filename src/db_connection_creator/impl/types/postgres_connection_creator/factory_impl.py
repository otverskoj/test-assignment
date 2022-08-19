from typing import Mapping, Any

from src.db_connection_creator.core.connection_creator import IDBConnectionCreator
from src.db_connection_creator.core.factory import IDBConnectionCreatorFactory
from src.db_connection_creator.impl.types.postgres_connection_creator.config import PostgresConnectionCreatorConfig
from src.db_connection_creator.impl.types.postgres_connection_creator.connection_creator_impl import \
    PostgresConnectionCreatorImpl


class PostgresConnectionCreatorFactory(IDBConnectionCreatorFactory):
    __slots__ = ('__settings',)

    def __init__(self, settings: Mapping[str, Any]):
        self.__settings = settings

    @classmethod
    def type(cls):
        return 'postgres'

    def get_connection_creator(self) -> IDBConnectionCreator:
        config = PostgresConnectionCreatorConfig(**self.__settings)
        return PostgresConnectionCreatorImpl(config)
