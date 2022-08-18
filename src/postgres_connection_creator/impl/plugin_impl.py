from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin.core.plugin import IPlugin
from src.postgres_connection_creator.core.connection_creator import PostgresConnection
from src.postgres_connection_creator.impl.config import PostgresConnectionCreatorConfig
from src.postgres_connection_creator.impl.connection_creator_impl import PostgresConnectionCreatorImpl


class PostgresConnectionCreatorPlugin(IPlugin):
    def __init__(
        self,
        config: PostgresConnectionCreatorConfig
    ) -> None:
        self.config = config

    def initialize(self) -> None:
        creator = PostgresConnectionCreatorImpl(self.config)
        connection = creator.get_connection()

        ioc.set_instance(PostgresConnection, connection)

    def deinitialize(self) -> None:
        conn = ioc.get_instance(PostgresConnection)
        if not conn.closed:
            conn.close()
