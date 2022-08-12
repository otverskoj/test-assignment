import psycopg2

from app.storage.repositories.postgres.settings_model import UserPostgresRepositorySettings


class PostgresConnectionCreator:
    # def __new__(cls, settings: UserPostgresRepositorySettings):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(PostgresConnectionCreator, cls).__new__(cls)
    #         cls.instance._connection = None
    #         cls.instance.settings = settings
    #     return cls.instance

    __slots__ = ('__connection', '__settings')

    def __init__(self, settings: UserPostgresRepositorySettings) -> None:
        self.__connection = None
        self.__settings = settings

    @property
    def connection(self) -> psycopg2.extensions.connection:
        if self.__connection is None:
            self.__connection = psycopg2.connect(
                dbname=self.__settings.db_name,
                user=self.__settings.db_user,
                password=self.__settings.db_password,
                host=self.__settings.db_host,
                port=self.__settings.db_port
            )
        return self.__connection
