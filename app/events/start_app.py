from typing import Callable

from app.ioc.ioc import ioc
from app.services.user_service import IUserService
from app.services.user_service_impl import UserServiceImpl
from app.settings.models.app import ApplicationSettings
from app.storage.repositories.factory_storage import IUserRepositoryFactoryStorage
from app.storage.repositories.factory_storage_impl import UserRepositoryFactoryStorageImpl
from app.storage.repositories.in_memory.factory import UserInMemoryRepositoryFactory
from app.storage.repositories.postgres.factory import UserPostgresRepositoryFactory
from app.storage.repositories.user_repository import IUserRepository


def create_start_app_handler(
    settings: ApplicationSettings,
) -> Callable:
    def start_app() -> None:
        user_repo_fac_storage = UserRepositoryFactoryStorageImpl()
        user_repo_fac_storage.register(UserInMemoryRepositoryFactory())
        user_repo_fac_storage.register(UserPostgresRepositoryFactory())
        ioc.set_instance(IUserRepositoryFactoryStorage, user_repo_fac_storage)

        user_repo_fac = user_repo_fac_storage.get_factory(
            settings.repository.type
        )
        user_repo = user_repo_fac.get_user_repository(
            settings.repository.settings
        )
        user_service = UserServiceImpl(user_repo=user_repo)
        ioc.set_instance(IUserService, user_service)
        ioc.set_instance(IUserRepository, user_repo)

    return start_app
