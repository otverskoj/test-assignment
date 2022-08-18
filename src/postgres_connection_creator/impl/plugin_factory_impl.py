from typing import Optional, Mapping, Any

from src.infrastructure.plugin.core.plugin import IPlugin
from src.infrastructure.plugin.core.plugin_factory import IPluginFactory
from src.postgres_connection_creator.impl.config import PostgresConnectionCreatorConfig
from src.postgres_connection_creator.impl.plugin_impl import PostgresConnectionCreatorPlugin


class PostgresConnectionCreatorPluginFactory(IPluginFactory):
    plugin_type = 'postgres_connection_creator'

    @classmethod
    def type(cls):
        return cls.plugin_type

    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        settings = settings or {}
        config = PostgresConnectionCreatorConfig(**settings)
        return PostgresConnectionCreatorPlugin(config)
