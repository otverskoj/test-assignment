from typing import Mapping, Any

from app.infrastructure.ioc.impl.ioc_impl import ioc
from app.mixin.plugin import IPlugin
from app.postgres.impl.config import PostgresRepositoryConfig
from app.postgres.core.connection_creator import PostgresConnection
from app.postgres.impl.connection_creator_impl import PostgresConnectionCreatorImpl


class PostgresPlugin(IPlugin):
    def initialize(self, config: Mapping[str, Any]) -> None:
        postgres_config = PostgresRepositoryConfig(**config['repository']['config'])
        conn = PostgresConnectionCreatorImpl(postgres_config).get_connection()
        ioc.set_instance(PostgresConnection, conn)

    def deinitialize(self) -> None:
        conn = ioc.get_instance(PostgresConnection)
        if not conn.closed():
            conn.close()

