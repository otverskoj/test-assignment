from typing import Mapping, Any

from app.ioc.ioc import ioc
from app.plugin import IPlugin
from app.postgres.config import PostgresRepositoryConfig
from app.postgres.connection_creator import (
    PostgresConnectionCreator,
    PostgresConnection
)


class PostgresPlugin(IPlugin):
    def initialize(self, config: Mapping[str, Any]) -> None:
        postgres_config = PostgresRepositoryConfig(**config['repository']['config'])
        conn = PostgresConnectionCreator(postgres_config).get_connection()
        ioc.set_instance(PostgresConnection, conn)

    def deinitialize(self) -> None:
        conn = ioc.get_instance(PostgresConnection)
        if conn.closed() == 0:
            conn.close()

