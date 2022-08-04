from typing import Optional

from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.in_memory.repository import UserInMemoryRepository
from app.settings.setting_models.app import ApplicationSettings


class UserInMemoryRepositoryFactory(IUserRepositoryFactory):
    def get_user_repository(
        self,
        settings: Optional[ApplicationSettings] = None
    ) -> IUserRepository:
        return UserInMemoryRepository()
