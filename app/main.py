from fastapi import FastAPI
from app.api.routers import users
from app.events.start_app import create_start_app_handler
from app.events.stop_app import create_stop_app_handler
from app.settings.settings import get_application_settings


def get_application() -> FastAPI:
    settings = get_application_settings()

    app = FastAPI()

    app.include_router(users.router)

    app.add_event_handler(
        "startup",
        create_start_app_handler(app, settings),
    )
    app.add_event_handler(
        "shutdown",
        create_stop_app_handler(app),
    )

    return app


app = get_application()
