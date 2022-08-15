from typing import Mapping, Any

from app.plugin import IPlugin
from app.user.repositories.factory_storage_impl import UserRepositoryFactoryStorageImpl
from app.user.repositories.in_memory.factory import UserInMemoryRepositoryFactory
from app.user.repositories.postgres.factory import UserPostgresRepositoryFactory
from app.user.service.user_service import IUserService
from app.user.service.user_service_impl import UserServiceImpl
from app.ioc.ioc import ioc
from app.postgres.connection_creator import PostgresConnection


class UserPlugin(IPlugin):
    def initialize(self, config: Mapping[str, Any]) -> None:
        storage = UserRepositoryFactoryStorageImpl()
        storage.register(UserInMemoryRepositoryFactory())
        storage.register(UserPostgresRepositoryFactory())

        fac = storage.get_factory(config['repository']['type'])

        conn = ioc.get_instance(PostgresConnection)
        repo = fac.get_user_repository(conn)

        service = UserServiceImpl(repo)
        ioc.set_instance(IUserService, service)

    def deinitialize(self) -> None:
        ioc.delete_instance(IUserService)
