from typing import Sequence

from src.infrastructure.plugin.core.plugin import IPlugin
from src.launcher.core.launcher import ILauncher


class Launcher(ILauncher):
    __slots__ = (
        '__plugins'
    )

    def __init__(
        self,
        plugins: Sequence[IPlugin]
    ) -> None:
        self.__plugins = plugins

    def handle_startup(self) -> None:
        for plugin in self.__plugins:
            self.__initialize_plugin(plugin)

    def __initialize_plugin(self, plugin: IPlugin) -> None:
        plugin.initialize()

    def handle_shutdown(self) -> None:
        for plugin in self.__plugins[::-1]:
            plugin.deinitialize()

    def __deinitialize_plugin(self, plugin: IPlugin) -> None:
        plugin.deinitialize()
