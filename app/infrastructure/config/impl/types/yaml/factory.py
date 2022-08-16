from typing import List

from app.infrastructure.config.impl.types.yaml.parser import YAMLConfigParser
from app.infrastructure.config.core.config_factory import IConfigFactory
from app.infrastructure.config.core.config_parser import IConfigParser


__all__ = ['YAMLConfigFactory']


class YAMLConfigFactory(IConfigFactory):
    __config_types = [
        'yaml',
        'yml'
    ]

    @classmethod
    def config_types(cls) -> List[str]:
        return cls.__config_types

    def get_parser(self) -> IConfigParser:
        return YAMLConfigParser()
