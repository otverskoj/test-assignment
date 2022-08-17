from app.infrastructure.config.config import get_application_config
from app.postgres.plugin import PostgresPlugin
from app.user.plugin import UserPlugin


def handle_startup(config_path: str) -> None:
    config = get_application_config(config_path)

    postgres_plugin = PostgresPlugin()
    postgres_plugin.initialize(config.dict())

    user_plugin = UserPlugin()
    user_plugin.initialize(config.dict())
