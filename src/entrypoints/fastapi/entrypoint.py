from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.infrastructure.config.config import get_application_config
from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.launcher.core.launcher import ILauncher
from src.launcher.impl.launcher_impl import Launcher


__all__ = [
    'get_app'
]


def get_app(settings_path: str) -> FastAPI:
    app = FastAPI()

    def handle_startup() -> None:

        ioc.set_instance(FastAPI, app)

        app_config = get_application_config(settings_path)

        launcher = Launcher(
            config=app_config
        )

        launcher.handle_startup()

    def handle_shutdown() -> None:
        launcher = ioc.get_instance(ILauncher)
        launcher.handle_shutdown()

    app.add_event_handler("startup", handle_startup)
    app.add_event_handler("shutdown", handle_shutdown)

    def exception_handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={
                "message": f"{exc}"
            }
        )

    app.add_exception_handler(Exception, exception_handler)

    return app
