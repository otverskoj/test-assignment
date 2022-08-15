from abc import ABC, abstractmethod
from typing import Type

from app.config.config_factory import IConfigFactory


class IConfigFactoryStorage(ABC):
    @abstractmethod
    def register(self, fac: IConfigFactory) -> None:
        pass

    @abstractmethod
    def unregister(self, fac_class: Type[IConfigFactory]) -> None:
        pass

    @abstractmethod
    def get_factory(self, config_type: str) -> IConfigFactory:
        pass
