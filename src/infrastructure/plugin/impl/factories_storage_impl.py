from typing import Dict, Type, Sequence, List

from src.infrastructure.plugin.core.factories_storage import IPluginFactoriesStorage
from src.infrastructure.plugin.core.plugin_factory import IPluginFactory


class PluginFactoriesStorageImpl(IPluginFactoriesStorage):
    __slots__ = ('__factories',)

    def __init__(self) -> None:
        self.__factories: Dict[str, IPluginFactory] = {}

    def register(self, fac: IPluginFactory) -> None:
        fac_type = fac.type()
        if fac_type in self.__factories:
            raise ValueError(f"This factory already registered")
        self.__factories[fac_type] = fac

    def unregister(self, fac_class: Type[IPluginFactory]) -> None:
        fac_type = fac_class.type()
        if fac_type not in self.__factories:
            raise KeyError(f"This factory not registered")
        self.__factories.pop(fac_type, None)

    def get_ordered_plugin_factories(
        self,
        factory_types: Sequence[str]
    ) -> Sequence[IPluginFactory]:
        factories: List[IPluginFactory] = []
        for factory_type in factory_types:
            if factory_type in self.__factories:
                factories.append(self.__factories[factory_type])
            else:
                raise KeyError(
                    f"This factory not registered"
                )
        return factories
