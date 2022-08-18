from abc import ABC, abstractmethod
from typing import Type, Sequence, Dict, List

from src.infrastructure.plugin.core.plugin_factory import IPluginFactory


class IPluginFactoriesStorage(ABC):
    __slots__ = ()

    @abstractmethod
    def register(self, fac: IPluginFactory) -> None:
        pass

    @abstractmethod
    def unregister(self, fac_class: Type[IPluginFactory]) -> None:
        pass

    @abstractmethod
    def get_ordered_plugin_factories(
        self,
        plugin_types: Sequence[str]
    ) -> Sequence[IPluginFactory]:
        pass
