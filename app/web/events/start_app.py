from typing import Callable

# from app.ioc.ioc import ioc
# from app.user.service import IUserService
# from app.user.service.user_service_impl import UserServiceImpl
# from app.config.models import ApplicationSettings
# from app.user.repositories.factory_storage import IUserRepositoryFactoryStorage
# from app.user.repositories.factory_storage_impl import UserRepositoryFactoryStorageImpl
# from app.user.repositories.in_memory import UserInMemoryRepositoryFactory
# from app.user.repositories.postgres.factory import UserPostgresRepositoryFactory
# from app.user.repositories.user_repository import IUserRepository


def create_start_app_handler() -> Callable:
    def start_app() -> None:
        pass

    return start_app
