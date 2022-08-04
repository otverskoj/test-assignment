from abc import ABC, abstractmethod
from typing import Optional

from app.storage.repositories.user_repository import IUserRepository
from app.settings.setting_models.app import ApplicationSettings


class IUserRepositoryFactory(ABC):
    @abstractmethod
    def get_user_repository(
        self,
        settings: Optional[ApplicationSettings] = None
    ) -> IUserRepository:
        pass
