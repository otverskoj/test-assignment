from typing import Optional, Mapping, Any

from app.user.repositories.user_repository import IUserRepository
from app.user.repositories.repository_factory import IUserRepositoryFactory
from app.user.repositories.postgres.repository import UserPostgresRepository
from app.postgres.connection_creator import PostgresConnection


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    __repo_type = 'postgres'

    @classmethod
    def repo_type(cls) -> str:
        return cls.__repo_type

    def get_user_repository(
        self,
        connection: Optional[PostgresConnection] = None
    ) -> IUserRepository:
        return UserPostgresRepository(connection)
