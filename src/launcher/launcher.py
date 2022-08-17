from typing import Sequence

from pydantic import BaseModel

from src.infrastructure.config.impl.application_config import ApplicationConfig
from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin_core.plugin import IPlugin
from src.launcher.bootstrap import bootstrap


class ApplicationPlugins(BaseModel):
    plugins: Sequence[IPlugin]


class Launcher:
    __slots__ = ('__plugins', '__config')

    def __init__(self, config: ApplicationConfig, plugins: Sequence[IPlugin]) -> None:
        self.__config = config
        self.__plugins = plugins

    def handle_startup(self) -> None:
        # bootstrap()
        # self.__plugins = ioc.get_instance(ApplicationPlugins).plugins
        for plugin in self.__plugins:
            self.__initialize_plugin(plugin)

    def __initialize_plugin(self, plugin: IPlugin) -> None:
        plugin.initialize()

    def handle_shutdown(self) -> None:
        for plugin in self.__plugins[::-1]:
            plugin.deinitialize()

    def __deinitialize_plugin(self, plugin: IPlugin) -> None:
        plugin.deinitialize()
