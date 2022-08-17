from typing import Optional, Mapping, Any

from src.infrastructure.plugin_core.plugin import IPlugin
from src.infrastructure.plugin_core.plugin_factory import PluginFactory
from src.user.impl.config import UserConfig
from src.user.impl.plugin_impl import UserPlugin


class UserPluginFactory(PluginFactory):
    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        settings = settings or {}
        config = UserConfig(**settings)
        return UserPlugin(config)
