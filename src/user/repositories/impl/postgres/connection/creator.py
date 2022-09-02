from typing import Any, Mapping

import psycopg2

from src.user.repositories.impl.postgres.connection.config import PostgresConnectionConfig


__all__ = [
    'PostgresConnectionCreator',
    'PostgresConnection'
]


PostgresConnection = psycopg2.extensions.connection


class PostgresConnectionCreator:
    def get_connection(
        self,
        settings: Mapping[str, Any]
    ) -> PostgresConnection:
        config = PostgresConnectionConfig(**settings)
        try:
            postgres = psycopg2.connect(
                dbname=config.name,
                user=config.user,
                password=config.password,
                host=config.host,
                port=config.port
            )
        except Exception:
            raise ConnectionError(
                f"Error to create postgres connection"
            ) from None
        return postgres
