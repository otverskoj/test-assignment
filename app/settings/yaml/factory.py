from typing import List

from app.settings.yaml.parser import YAMLSettingsParser
from app.settings.settings_factory import ISettingsFactory
from app.settings.settings_parser import ISettingsParser


__all__ = ['YAMLSettingsFactory']


class YAMLSettingsFactory(ISettingsFactory):
    settings_types = [
        'yaml',
        'yml'
    ]

    @classmethod
    def types(cls) -> List[str]:
        return cls.settings_types

    def get_parser(self) -> ISettingsParser:
        return YAMLSettingsParser()
