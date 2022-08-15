from typing import Any, Mapping, Optional

from app.user.repositories.repository_factory import IUserRepositoryFactory
from app.user.repositories.user_repository import IUserRepository
from app.user.repositories.in_memory.repository import UserInMemoryRepository


class UserInMemoryRepositoryFactory(IUserRepositoryFactory):
    __repo_type = 'in-memory'

    @classmethod
    def repo_type(cls) -> str:
        return cls.__repo_type

    def get_user_repository(
        self,
        repo_config: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        return UserInMemoryRepository()
