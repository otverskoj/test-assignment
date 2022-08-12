from typing import List

from app.settings.json.parser import JSONSettingsParser
from app.settings.settings_factory import ISettingsFactory
from app.settings.settings_parser import ISettingsParser


__all__ = ['JSONSettingsFactory']


class JSONSettingsFactory(ISettingsFactory):
    __settings_types = [
        'json'
    ]

    @classmethod
    def settings_types(cls) -> List[str]:
        return cls.__settings_types

    def get_parser(self) -> ISettingsParser:
        return JSONSettingsParser()
