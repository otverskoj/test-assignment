import psycopg2

from src.db_connection_creator.core.connection_creator import IDBConnectionCreator
from src.db_connection_creator.impl.types.postgres_connection_creator.config import PostgresConnectionCreatorConfig


PostgresConnection = psycopg2.extensions.connection


class PostgresConnectionCreatorImpl(IDBConnectionCreator):
    @classmethod
    def type(cls):
        pass

    __slots__ = ('__config',)

    def __init__(self, config: PostgresConnectionCreatorConfig) -> None:
        self.__config = config

    def get_connection(self) -> PostgresConnection:
        try:
            postgres = psycopg2.connect(
                dbname=self.__config.db_name,
                user=self.__config.db_user,
                password=self.__config.db_password,
                host=self.__config.db_host,
                port=self.__config.db_port
            )
        except Exception as e:
            raise ConnectionError(
                f"Error to create postgres connection"
            ) from e
        return postgres
