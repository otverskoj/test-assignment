from typing import Optional, Mapping, Any

from src.infrastructure.plugin.core.plugin import IPlugin
from src.infrastructure.plugin.core.plugin_factory import IPluginFactory
from src.user.impl.config import UserConfig
from src.user.impl.plugin_impl import UserPlugin


class UserPluginFactory(IPluginFactory):
    plugin_type = 'user'
    @classmethod
    def type(cls):
        return cls.plugin_type

    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        settings = settings or {}
        config = UserConfig(**settings)
        return UserPlugin(config)
