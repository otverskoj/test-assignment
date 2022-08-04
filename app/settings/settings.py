from functools import lru_cache

from app.settings.setting_models.app import ApplicationSettings


@lru_cache
def read_application_settings() -> ApplicationSettings:
    return ApplicationSettings()
