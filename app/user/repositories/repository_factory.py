from abc import ABC, abstractmethod
from typing import Optional, Mapping, Any

from app.user.repositories.user_repository import IUserRepository
from app.postgres.connection_creator import PostgresConnection


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
