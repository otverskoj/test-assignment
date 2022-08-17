from typing import Any, Mapping, Optional

from src.postgres_connection_creator.impl.plugin_factory_impl import PostgresConnectionCreatorPluginFactory
from src.postgres_connection_creator.impl.plugin_impl import PostgresConnectionCreatorPlugin


def postgres_connection_creator_startup(
    settings: Optional[Mapping[str, Any]] = None
) -> None:
    fac = PostgresConnectionCreatorPluginFactory()
    plugin = fac.get_plugin(settings)
    # ioc...

    # plugin = PostgresConnectionCreatorPlugin(settings)
    # plugin.initialize()
    # TODO: плагин нужно будет деинициализировать, но для этого к нему должен быть доступ.
    #  В IoC-контейнер складывать его не получится, так как плагин не один.
    #  Решение: задавать список плагинов для запуска в конфиг-файле, сохранять в pydantic-модель,
    #  а инициализировать/деинициализировать в классе Launcher'а
