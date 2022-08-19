from typing import Mapping, Any

from src.db_connection_creator.plugin.config import DBConnectionCreatorPluginConfig
from src.db_connection_creator.plugin.plugin_impl import DBConnectionCreatorPlugin
from src.infrastructure.plugin.core.plugin import IPlugin
from src.infrastructure.plugin.core.plugin_factory import IPluginFactory


class DBConnectionCreatorPluginFactory(IPluginFactory):
    __slots__ = ()

    @classmethod
    def type(cls):
        pass

    def get_plugin(self, settings: Mapping[str, Any]) -> IPlugin:
        config = DBConnectionCreatorPluginConfig(**settings)
        return DBConnectionCreatorPlugin(config=config)
