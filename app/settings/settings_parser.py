from abc import ABC, abstractmethod

from app.settings.models.app import ApplicationSettings


class ISettingsParser(ABC):
    @abstractmethod
    def get_settings(self, settings_path: str) -> ApplicationSettings:
        pass
