from functools import lru_cache

from app.settings.setting_models.app import ApplicationSettings, RepositorySettings


@lru_cache
def read_application_settings() -> ApplicationSettings:
    repo = RepositorySettings()
    return ApplicationSettings(repository=repo)
