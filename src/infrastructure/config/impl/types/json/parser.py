import json
from typing import Any, Dict

from src.infrastructure.config.core.config_parser import IConfigParser
from src.infrastructure.config.impl.application_config import ApplicationConfig


class JSONConfigParser(IConfigParser):
    def __init__(self, encoding: str = 'utf-8') -> None:
        self.encoding = encoding

    def get_config(self, config_path: str) -> ApplicationConfig:
        raw_config = self.__read_config_file(config_path)
        return ApplicationConfig(**raw_config)

    def __read_config_file(self, config_path: str) -> Dict[str, Any]:
        with open(config_path, encoding=self.encoding) as f:
            raw = json.load(f)
        return raw
