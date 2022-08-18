from typing import Any, Dict, Type

from src.infrastructure.config.core.config_factory import IConfigFactory
from src.infrastructure.config.core.factories_storage import IConfigFactoriesStorage


class ConfigFactoriesStorageImpl(IConfigFactoriesStorage):
    __slots__ = ('__instances',)

    def __init__(self) -> None:
        self.__instances: Dict[str, Any] = {}

    def register(self, fac: IConfigFactory) -> None:
        config_types = fac.config_types()
        for config_type in config_types:
            if config_type in self.__instances:
                raise KeyError(
                    f'Factory for {config_type} config already registered'
                )
            self.__instances[config_type] = fac

    def unregister(self, fac_class: Type[IConfigFactory]) -> None:
        config_types = fac_class.config_types()
        for config_type in config_types:
            if config_type not in self.__instances:
                raise KeyError(
                    f'Factory for {config_type} config not registered'
                )
            del self.__instances[config_type]

    def get_factory(self, config_type: str) -> IConfigFactory:
        if config_type not in self.__instances:
            raise KeyError(
                f'Factory for {config_type} config not registered'
            )
        return self.__instances[config_type]
