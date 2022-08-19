from typing import Mapping, Any

from src.infrastructure.plugin.core.plugin import IPlugin
from src.infrastructure.plugin.core.plugin_factory import IPluginFactory
from src.user.plugin.config import UserPluginConfig
from src.user.plugin.plugin_impl import UserPlugin


class UserPluginFactory(IPluginFactory):
    @classmethod
    def type(cls):
        return 'user'

    def get_plugin(
        self,
        settings: Mapping[str, Any]
    ) -> IPlugin:
        config = UserPluginConfig(**settings)
        return UserPlugin(config=config)
