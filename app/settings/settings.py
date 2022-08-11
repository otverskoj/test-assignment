import os
from functools import lru_cache
from pathlib import Path

from app.settings.factory_storage import SettingsFactoryStorage
from app.settings.json.factory import JSONSettingsFactory
from app.settings.models.app import ApplicationSettings
from app.settings.yaml.factory import YAMLSettingsFactory


@lru_cache
def get_application_settings() -> ApplicationSettings:
    settings_path = os.getenv('SETTINGS_PATH')
    settings_storage = SettingsFactoryStorage()

    settings_storage.register(JSONSettingsFactory())
    settings_storage.register(YAMLSettingsFactory())

    fac = settings_storage.get_factory(_get_settings_type(settings_path))
    parser = fac.get_parser()
    return parser.get_settings(settings_path)


def _get_settings_type(settings_path: str) -> str:
    settings_path = Path(settings_path)
    if not settings_path.exists():
        raise FileNotFoundError(f"{settings_path} is not valid path")
    return settings_path.suffix.split('.')[-1]
