from abc import ABC, abstractmethod
from typing import Type

from app.settings.settings_factory import ISettingsFactory


class ISettingsFactoryStorage(ABC):
    @abstractmethod
    def register(self, fac: ISettingsFactory) -> None:
        pass

    @abstractmethod
    def unregister(self, fac_class: Type[ISettingsFactory]) -> None:
        pass

    @abstractmethod
    def get_factory(self, settings_type: str) -> ISettingsFactory:
        pass
