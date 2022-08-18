from abc import ABC, abstractmethod
from typing import Optional, Mapping, Any

from src.infrastructure.plugin.core.plugin import IPlugin


class IPluginFactory(ABC):
    @classmethod
    @abstractmethod
    def type(cls):
        pass

    @abstractmethod
    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        pass
