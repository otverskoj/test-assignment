from typing import Any, Mapping, Optional

from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.in_memory.repository import UserInMemoryRepository
from app.settings.models.app import ApplicationSettings


class UserInMemoryRepositoryFactory(IUserRepositoryFactory):
    __repo_type = 'in-memory'

    @classmethod
    def repo_type(cls) -> str:
        return cls.__repo_type

    def get_user_repository(
        self,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        return UserInMemoryRepository()
