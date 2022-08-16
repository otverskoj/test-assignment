import yaml
from typing import Any, Dict

from app.infrastructure.config.impl.models.app import ApplicationConfig, RepositoryConfig
from app.infrastructure.config.core.config_parser import IConfigParser


class YAMLConfigParser(IConfigParser):
    def __init__(self, encoding: str = 'utf-8') -> None:
        self.encoding = encoding

    def get_config(self, config_path: str) -> ApplicationConfig:
        raw_config = self.__read_config_file(config_path)
        repo = RepositoryConfig(**raw_config)
        return ApplicationConfig(repository=repo, **raw_config)

    def __read_config_file(self, config_path: str) -> Dict[str, Any]:
        with open(config_path, encoding=self.encoding) as f:
            raw = yaml.load(f, yaml.BaseLoader)
        return raw
