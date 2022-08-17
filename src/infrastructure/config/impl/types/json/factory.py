from typing import List

from src.infrastructure.config.core.config_factory import IConfigFactory
from src.infrastructure.config.core.config_parser import IConfigParser
from src.infrastructure.config.impl.types.json.parser import JSONConfigParser


__all__ = ['JSONConfigFactory']


class JSONConfigFactory(IConfigFactory):
    __config_types = [
        'json'
    ]

    @classmethod
    def config_types(cls) -> List[str]:
        return cls.__config_types

    def get_parser(self) -> IConfigParser:
        return JSONConfigParser()
