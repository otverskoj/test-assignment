from typing import List

from app.settings.json.parser import JSONSettingsParser
from app.settings.settings_factory import ISettingsFactory
from app.settings.settings_parser import ISettingsParser


__all__ = ['JSONSettingsFactory']


class JSONSettingsFactory(ISettingsFactory):
    settings_types = [
        'json'
    ]

    @classmethod
    def types(cls) -> List[str]:
        return cls.settings_types

    def get_parser(self) -> ISettingsParser:
        return JSONSettingsParser()
