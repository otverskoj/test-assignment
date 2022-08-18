from fastapi import FastAPI

from src.infrastructure.config.config import get_application_config
from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.infrastructure.plugin.impl.factories_storage_impl import PluginFactoriesStorageImpl
from src.launcher.core.launcher import ILauncher
from src.launcher.impl.launcher_impl import Launcher
from src.postgres_connection_creator.impl.plugin_factory_impl import PostgresConnectionCreatorPluginFactory
from src.user.impl.plugin_factory import UserPluginFactory


def get_app(settings_path: str) -> FastAPI:
    app = FastAPI()

    def handle_startup() -> None:
        ioc.set_instance(FastAPI, app)

        plugin_factories_storage = PluginFactoriesStorageImpl()
        plugin_factories_storage.register(PostgresConnectionCreatorPluginFactory())
        plugin_factories_storage.register(UserPluginFactory())

        app_config = get_application_config(settings_path)

        plugin_factories = plugin_factories_storage.get_ordered_plugin_factories(
            factory_types=list(app_config.plugins.keys())
        )

        plugins = [
            plugin_fac.get_plugin(
                settings=app_config.plugins[plugin_fac.type()]
            )
            for plugin_fac in plugin_factories
        ]

        # postgres_plugin_fac = PostgresConnectionCreatorPluginFactory()
        # postgres_plugin = postgres_plugin_fac.get_plugin(
        #     settings=app_config.plugins['postgres_connection_creator']
        # )

        # user_plugin_fac = UserPluginFactory()
        # user_plugin = user_plugin_fac.get_plugin(
        #     settings=app_config.plugins['user']
        # )

        launcher = Launcher(
            plugins=plugins
        )
        ioc.set_instance(ILauncher, launcher)

        launcher.handle_startup()

    def handle_shutdown() -> None:
        launcher = ioc.get_instance(ILauncher)
        launcher.handle_shutdown()

    app.add_event_handler("startup", handle_startup)
    app.add_event_handler("shutdown", handle_shutdown)

    return app
