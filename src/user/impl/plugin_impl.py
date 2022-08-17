from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin_core.plugin import IPlugin
from src.postgres_connection_creator.core.connection_creator import PostgresConnection
from src.user.impl.config import UserConfig
from src.user.repositories.impl.factory_storage_impl import UserRepositoryFactoryStorageImpl
from src.user.repositories.impl.in_memory.factory import UserInMemoryRepositoryFactory
from src.user.repositories.impl.postgres.factory import UserPostgresRepositoryFactory
from src.user.service.core.user_service import IUserService
from src.user.service.impl.user_service_impl import UserServiceImpl


class UserPlugin(IPlugin):
    def __init__(self, config: UserConfig) -> None:
        self.config = config

    def initialize(self) -> None:
        storage = UserRepositoryFactoryStorageImpl()
        storage.register(UserInMemoryRepositoryFactory())
        storage.register(UserPostgresRepositoryFactory())

        fac = storage.get_factory(self.config.repository.type)

        conn = ioc.get_instance(PostgresConnection)
        repo = fac.get_user_repository(conn)

        service = UserServiceImpl(repo)
        ioc.set_instance(IUserService, service)

    def deinitialize(self) -> None:
        ioc.delete_instance(IUserService)
