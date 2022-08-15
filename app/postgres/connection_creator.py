import psycopg2

from app.postgres.config import PostgresRepositoryConfig


PostgresConnection = psycopg2.extensions.connection


class PostgresConnectionCreator:
    __slots__ = ('__connection', '__config')

    def __init__(self, config: PostgresRepositoryConfig) -> None:
        self.__connection: Optional[PostgresConnection] = None
        self.__config = config

    def get_connection(self) -> PostgresConnection:
        if self.__connection is None:
            self.__create_connection()
        return self.__connection

    def __create_connection(self) -> None:
        self.__connection = psycopg2.connect(
            dbname=self.__config.db_name,
            user=self.__config.db_user,
            password=self.__config.db_password,
            host=self.__config.db_host,
            port=self.__config.db_port
        )
