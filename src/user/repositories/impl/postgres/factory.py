from typing import Optional, Mapping, Any

from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.postgres_connection_creator.core.connection_creator import PostgresConnection
from src.user.repositories.core.repository_factory import IUserRepositoryFactory
from src.user.repositories.core.user_repository import IUserRepository
from src.user.repositories.impl.postgres.repository import UserPostgresRepository


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    __repo_type = 'postgres'

    @classmethod
    def repo_type(cls) -> str:
        return cls.__repo_type

    def get_user_repository(
        self,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        conn = ioc.get_instance(PostgresConnection)
        return UserPostgresRepository(conn)
