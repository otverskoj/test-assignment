from abc import ABC, abstractmethod
from typing import Optional, Mapping, Any

from app.storage.repositories.user_repository import IUserRepository


class IUserRepositoryFactory(ABC):
    @abstractmethod
    def get_user_repository(
        self,
        repo_type: str,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        pass
