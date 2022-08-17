from fastapi import FastAPI

from src.infrastructure.config.config import get_application_config
from src.launcher.launcher import Launcher

app = FastAPI()
launcher: Launcher


def handle_startup() -> None:
    global launcher

    app_config = get_application_config('configs/application_config.yml')

    launcher = Launcher(
        app_config
    )
    launcher.handle_startup()


def handle_shutdown() -> None:
    global launcher
    launcher.handle_shutdown()


app.add_event_handler("startup", handle_startup)
app.add_event_handler("shutdown", handle_shutdown)
