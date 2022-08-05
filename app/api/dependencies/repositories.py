from fastapi import Depends

from app.settings.setting_models.app import ApplicationSettings
from app.settings.settings import read_application_settings
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.factory_storage import UserRepositoryFactoryStorage


def get_user_repository(
    settings: ApplicationSettings = Depends(read_application_settings)
) -> IUserRepository:
    fac = _get_user_repo_factory(settings.repository_type)
    return fac.get_user_repository(settings)


def _get_user_repo_factory(repo_type: str) -> IUserRepositoryFactory:
    storage = _get_user_repo_factory_storage()
    return storage.get_factory(repo_type)


def _get_user_repo_factory_storage() -> UserRepositoryFactoryStorage:
    return UserRepositoryFactoryStorage()
