from typing import Any, Dict, Type

from app.settings.json.factory import JSONSettingsFactory
from app.settings.settings_factory import ISettingsFactory
from app.settings.yaml.factory import YAMLSettingsFactory


class SettingsFactoryStorage:
    __slots__ = ('__instances',)

    def __init__(self) -> None:
        self.__instances: Dict[str, Any] = {}

    def register(self, fac: ISettingsFactory) -> None:
        settings_types = fac.settings_types()
        for settings_type in settings_types:
            if settings_type in self.__instances:
                raise KeyError(
                    f'Factory for {settings_type} settings already registered'
                )
            self.__instances[settings_type] = fac

    def unregister(self, fac_class: Type[ISettingsFactory]) -> None:
        settings_types = fac_class.settings_types()
        for settings_type in settings_types:
            if settings_type not in self.__instances:
                raise KeyError(
                    f'Factory for {settings_type} settings not registered'
                )
            del self.__instances[settings_type]

    def get_factory(self, settings_type: str) -> ISettingsFactory:
        if settings_type not in self.__instances:
            raise KeyError(
                f'Factory for {settings_type} settings not registered'
            )
        return self.__instances[settings_type]


if __name__ == '__main__':
    from pprint import pprint

    storage = SettingsFactoryStorage()

    storage.register(JSONSettingsFactory())
    fac = storage.get_factory('json')
    parser = fac.get_parser()
    settings = parser.get_settings('./example/settings.json')
    pprint(settings.dict())

    storage.register(YAMLSettingsFactory())
    fac = storage.get_factory('yml')
    parser = fac.get_parser()
    settings = parser.get_settings('./example/settings.yaml')
    pprint(settings.dict())
