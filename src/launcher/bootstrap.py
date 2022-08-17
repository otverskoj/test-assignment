from src.infrastructure.config.impl.application_config import ApplicationConfig
from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.postgres_connection_creator.startup import postgres_connection_creator_startup
from src.user.startup import user_startup


def bootstrap() -> None:
    config = ioc.get_instance(ApplicationConfig)

    postgres_connection_creator_startup(config.connection_creator)
    user_startup(config.user)
