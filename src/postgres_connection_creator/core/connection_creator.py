from abc import ABC, abstractmethod

import psycopg2


PostgresConnection = psycopg2.extensions.connection


class IPostgresConnectionCreator(ABC):
    __slots__ = ()

    @abstractmethod
    def get_connection(self) -> PostgresConnection:
        pass
