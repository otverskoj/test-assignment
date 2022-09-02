from typing import List

from src.infrastructure.config.impl.application_config import ApplicationConfig
from src.infrastructure.plugin.core.plugin import IPlugin
from src.launcher.core.launcher import ILauncher
from src.user.plugin.plugin_factory import UserPluginFactory


class Launcher(ILauncher):
    __slots__ = (
        '__config',
        '__factories_types',
        '__plugins'
    )

    def __init__(self, config: ApplicationConfig) -> None:
        self.__config = config
        self.__plugins: List[IPlugin] = []

    def handle_startup(self) -> None:
        user_plugin_fac = UserPluginFactory()
        user_plugin = user_plugin_fac.get_plugin(self.__config.services.user)
        self.__plugins.append(user_plugin)

        for plugin in self.__plugins:
            self.__initialize_plugin(plugin)

    def __initialize_plugin(self, plugin: IPlugin) -> None:
        plugin.initialize()

    def handle_shutdown(self) -> None:
        for plugin in self.__plugins[::-1]:
            self.__deinitialize_plugin(plugin)

    def __deinitialize_plugin(self, plugin: IPlugin) -> None:
        plugin.deinitialize()
