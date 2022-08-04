import psycopg2

from app.storage.repositories.postgres.settings_model import UserPostgresRepositorySettings


class PostgresConnectionCreator:
    def __new__(cls, settings: UserPostgresRepositorySettings):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostgresConnectionCreator, cls).__new__(cls)
            cls.instance._connection = None
            cls.instance.settings = settings
        return cls.instance

    @property
    def connection(self) -> psycopg2.extensions.connection:
        if self._connection is None:
            self._connection = psycopg2.connect(
                dbname=self.settings.db_name,
                user=self.settings.db_user,
                password=self.settings.db_password,
                host=self.settings.db_host,
                port=self.settings.db_port
            )
        return self._connection
