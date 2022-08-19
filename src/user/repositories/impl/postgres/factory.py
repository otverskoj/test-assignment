from typing import Optional, Mapping, Any

from src.db_connection_creator.core.factory import IDBConnectionCreatorFactory
from src.user.repositories.core.repository_factory import IUserRepositoryFactory
from src.user.repositories.core.user_repository import IUserRepository
from src.user.repositories.impl.postgres.repository import UserPostgresRepository


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    __slots__ = (
        '__db_conn_creator_fac',
    )

    def __init__(self, db_conn_creator_fac: IDBConnectionCreatorFactory) -> None:
        self.__db_conn_creator_fac = db_conn_creator_fac

    @classmethod
    def repo_type(cls) -> str:
        return 'postgres'

    def get_user_repository(
        self,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        db_conn_creator = self.__db_conn_creator_fac.get_connection_creator()
        conn = db_conn_creator.get_connection()
        return UserPostgresRepository(conn)
