from abc import ABC, abstractmethod
from typing import Type

from src.infrastructure.config.core.config_factory import IConfigFactory


class IConfigFactoriesStorage(ABC):
    @abstractmethod
    def register(self, fac: IConfigFactory) -> None:
        pass

    @abstractmethod
    def unregister(self, fac_class: Type[IConfigFactory]) -> None:
        pass

    @abstractmethod
    def get_factory(self, config_type: str) -> IConfigFactory:
        pass
