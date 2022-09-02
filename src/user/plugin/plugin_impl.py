from fastapi import FastAPI

from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin.core.plugin import IPlugin
from src.user.plugin.config import UserPluginConfig
from src.user.repositories.impl.factory_storage_impl import UserRepositoryFactoriesStorageImpl
from src.user.repositories.impl.in_memory.factory import UserInMemoryRepositoryFactory
from src.user.repositories.impl.postgres.factory import UserPostgresRepositoryFactory
from src.user.service.core.user_service import IUserService
from src.user.service.impl.user_service_impl import UserServiceImpl
from src.user.views.models.response import UserResponse
from src.user.views.user_views import UserViews


class UserPlugin(IPlugin):
    __slots__ = ('__config',)

    def __init__(self, config: UserPluginConfig) -> None:
        self.__config = config

    def initialize(self) -> None:
        # repo startup
        storage = UserRepositoryFactoriesStorageImpl()
        storage.register(UserInMemoryRepositoryFactory)
        storage.register(UserPostgresRepositoryFactory)

        fac = storage.get_factory(repo_type=self.__config.repo_type)()

        repo = fac.get_user_repository(repo_settings=self.__config.repository)

        # service startup
        service = UserServiceImpl(repo)
        ioc.set_instance(IUserService, service)

        # views startup
        user_views = UserViews(service)

        app = ioc.get_instance(FastAPI)

        app.add_api_route(
            path='/users/{user_id}',
            endpoint=user_views.get_user_by_id,
            response_model=UserResponse,
            methods=['get']
        )
        app.add_api_route(
            path='/users/',
            endpoint=user_views.create_user,
            response_model=UserResponse,
            status_code=201,
            methods=['post']
        )
        app.add_api_route(
            path='/users/{user_id}',
            endpoint=user_views.update_user,
            response_model=UserResponse,
            methods=['put']
        )
        app.add_api_route(
            path='/users/{user_id}',
            endpoint=user_views.delete_user,
            status_code=204,
            methods=['delete']
        )

        ioc.set_instance(FastAPI, app)

    def deinitialize(self) -> None:
        ioc.delete_instance(IUserService)
