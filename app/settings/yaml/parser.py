import yaml
from typing import Any, Dict

from app.settings.models.app import ApplicationSettings, RepositorySettings
from app.settings.settings_parser import ISettingsParser


class YAMLSettingsParser(ISettingsParser):
    def __init__(self, encoding: str = 'utf-8') -> None:
        self.encoding = encoding

    def get_settings(self, settings_path: str) -> ApplicationSettings:
        raw_settings = self.__read_settings_file(settings_path)
        repo = RepositorySettings(**raw_settings)
        return ApplicationSettings(repository=repo, **raw_settings)

    def __read_settings_file(self, settings_path: str) -> Dict[str, Any]:
        with open(settings_path, encoding=self.encoding) as f:
            raw = yaml.load(f, yaml.BaseLoader)
        return raw
