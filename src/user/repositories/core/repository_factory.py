from abc import ABC, abstractmethod
from typing import Optional, Any, Mapping

from src.user.repositories.core.user_repository import IUserRepository


class IUserRepositoryFactory(ABC):
    @classmethod
    @abstractmethod
    def repo_type(cls) -> str:
        pass

    @abstractmethod
    def get_user_repository(
        self,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        pass
