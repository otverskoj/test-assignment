from abc import abstractmethod, ABC
from typing import List
from app.settings.settings_parser import ISettingsParser


__all__ = ['ISettingsFactory']


class ISettingsFactory(ABC):
    @classmethod
    @abstractmethod
    def types(cls) -> List[str]:
        pass

    @abstractmethod
    def get_parser(self) -> ISettingsParser:
        pass
