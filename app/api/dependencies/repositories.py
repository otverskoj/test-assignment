from typing import Optional, Mapping, Any

from fastapi import Depends

from app.settings.settings import get_application_settings
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.factory_storage import UserRepositoryFactoryStorage


def get_user_repository(
    app_settings: Optional[Mapping[str, Any]] = Depends(get_application_settings)
) -> IUserRepository:
    fac = _get_user_repo_factory(app_settings.repository.type)
    return fac.get_user_repository(
        repo_settings=app_settings.repository.settings,
    )


def _get_user_repo_factory(repo_type: str) -> IUserRepositoryFactory:
    storage = _get_user_repo_factory_storage()
    return storage.get_factory(repo_type)


def _get_user_repo_factory_storage() -> UserRepositoryFactoryStorage:
    return UserRepositoryFactoryStorage()
