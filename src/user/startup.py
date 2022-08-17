from typing import Optional, Mapping, Any

from src.user.impl.plugin_factory import UserPluginFactory


def user_startup(
    settings: Optional[Mapping[str, Any]] = None
) -> None:
    fac = UserPluginFactory()
    plugin = fac.get_plugin(settings)
    # ioc...