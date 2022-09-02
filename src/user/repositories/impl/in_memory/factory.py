from typing import Any, Mapping, Optional

from src.user.repositories.core.repository_factory import IUserRepositoryFactory
from src.user.repositories.core.user_repository import IUserRepository
from src.user.repositories.impl.in_memory.repository import UserInMemoryRepository


class UserInMemoryRepositoryFactory(IUserRepositoryFactory):
    @classmethod
    def repo_type(cls) -> str:
        return 'in-memory'

    def get_user_repository(
        self,
        repo_settings: Mapping[str, Any]
    ) -> IUserRepository:
        return UserInMemoryRepository()
