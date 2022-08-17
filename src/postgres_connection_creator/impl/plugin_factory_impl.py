from typing import Optional, Mapping, Any

from src.infrastructure.plugin_core.plugin import IPlugin
from src.infrastructure.plugin_core.plugin_factory import PluginFactory
from src.postgres_connection_creator.impl.config import PostgresConnectionCreatorConfig
from src.postgres_connection_creator.impl.plugin_impl import PostgresConnectionCreatorPlugin


class PostgresConnectionCreatorPluginFactory(PluginFactory):
    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        settings = settings or {}
        config = PostgresConnectionCreatorConfig(**settings)
        return PostgresConnectionCreatorPlugin(config)
