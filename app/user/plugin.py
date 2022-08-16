from typing import Mapping, Any

from app.mixin.plugin import IPlugin
from app.user.repositories.impl.factory_storage_impl import UserRepositoryFactoryStorageImpl
from app.user.repositories.impl.in_memory.factory import UserInMemoryRepositoryFactory
from app.user.repositories.impl.postgres.factory import UserPostgresRepositoryFactory
from app.user.service.core.user_service import IUserService
from app.user.service.impl.user_service_impl import UserServiceImpl
from app.infrastructure.ioc.impl.ioc_impl import ioc
from app.postgres.impl.connection_creator_impl import PostgresConnection


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
