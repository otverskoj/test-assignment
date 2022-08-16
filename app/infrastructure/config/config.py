from functools import lru_cache
from pathlib import Path

from app.infrastructure.config.impl.factory_storage_impl import ConfigFactoryStorageImpl
from app.infrastructure.config.impl.types.json.factory import JSONConfigFactory
from app.infrastructure.config.impl.models.app import ApplicationConfig
from app.infrastructure.config.impl.types.yaml.factory import YAMLConfigFactory


__all__ = ('get_application_config',)


@lru_cache
def get_application_config(config_path: str) -> ApplicationConfig:
    config_storage = ConfigFactoryStorageImpl()

    config_storage.register(JSONConfigFactory())
    config_storage.register(YAMLConfigFactory())

    fac = config_storage.get_factory(_get_config_type(config_path))
    parser = fac.get_parser()
    config = parser.get_config(config_path)

    # ioc.set_instance(ApplicationConfig, config)

    return config


def _get_config_type(config_path: str) -> str:
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"{config_path} is not valid path")
    return config_path.suffix.split('.')[-1]
