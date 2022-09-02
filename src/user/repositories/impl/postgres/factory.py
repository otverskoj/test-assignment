from typing import Mapping, Any

from src.user.repositories.core.repository_factory import IUserRepositoryFactory
from src.user.repositories.core.user_repository import IUserRepository
from src.user.repositories.impl.config import Repository
from src.user.repositories.impl.postgres.connection.creator import PostgresConnectionCreator
from src.user.repositories.impl.postgres.repository import UserPostgresRepository


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    @classmethod
    def repo_type(cls) -> str:
        return 'postgres'

    def get_user_repository(
        self,
        repo_settings: Mapping[str, Any]
    ) -> IUserRepository:
        # db_conn_creator = self.__db_conn_creator_fac.get_connection_creator()
        # conn = db_conn_creator.get_connection()
        config = Repository(**repo_settings)

        creator = PostgresConnectionCreator()
        conn = creator.get_connection(config.settings)

        return UserPostgresRepository(conn)
