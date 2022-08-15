from typing import Mapping, Any

from fastapi import FastAPI

from app.plugin import IPlugin
from .events.start_app import create_start_app_handler
from .events.stop_app import create_stop_app_handler
from ..ioc.ioc import ioc
from .routers import users


class WebPlugin(IPlugin):
    def initialize(self, config: Mapping[str, Any]) -> None:
        app = FastAPI()

        app.include_router(users.router)

        app.add_event_handler(
            "startup",
            create_start_app_handler(),
        )
        app.add_event_handler(
            "shutdown",
            create_stop_app_handler(app),
        )

        ioc.set_instance(FastAPI, app)

    def deinitialize(self) -> None:
        ioc.delete_instance(FastAPI)
