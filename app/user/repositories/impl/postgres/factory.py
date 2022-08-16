from typing import Optional

from app.user.repositories.core.user_repository import IUserRepository
from app.user.repositories.core.repository_factory import IUserRepositoryFactory
from app.user.repositories.impl.postgres.repository import UserPostgresRepository
from app.postgres.impl.connection_creator_impl import PostgresConnection


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
