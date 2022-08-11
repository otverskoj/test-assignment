from typing import Callable

from fastapi import FastAPI

from app.settings.models.app import ApplicationSettings


def create_start_app_handler(
    app: FastAPI,
    settings: ApplicationSettings,
) -> Callable:
    def start_app() -> None:
        print('App is starting up...')

    return start_app
