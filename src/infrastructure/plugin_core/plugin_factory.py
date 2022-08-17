from abc import ABC, abstractmethod
from typing import Optional, Mapping, Any

from src.infrastructure.plugin_core.plugin import IPlugin


class PluginFactory(ABC):
    @abstractmethod
    def get_plugin(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IPlugin:
        pass
