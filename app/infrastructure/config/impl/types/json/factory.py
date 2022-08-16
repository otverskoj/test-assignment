from typing import List

from app.infrastructure.config.impl.types.json.parser import JSONConfigParser
from app.infrastructure.config.core.config_factory import IConfigFactory
from app.infrastructure.config.core.config_parser import IConfigParser


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
