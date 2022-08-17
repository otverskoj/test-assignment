from abc import ABC, abstractmethod

from src.infrastructure.config.impl.application_config import ApplicationConfig


class IConfigParser(ABC):
    @abstractmethod
    def get_config(self, config_path: str) -> ApplicationConfig:
        pass
