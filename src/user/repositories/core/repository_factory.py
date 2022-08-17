from abc import ABC, abstractmethod
from typing import Optional

from app.user.repositories.core.user_repository import IUserRepository
from app.postgres.impl.connection_creator_impl import PostgresConnection


class IUserRepositoryFactory(ABC):
    @classmethod
    @abstractmethod
    def repo_type(cls) -> str:
        pass

    @abstractmethod
    def get_user_repository(
        self,
        connection: Optional[PostgresConnection] = None
    ) -> IUserRepository:
        pass
