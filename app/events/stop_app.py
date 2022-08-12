from typing import Callable

from fastapi import FastAPI

from app.ioc.ioc import ioc


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        ioc.delete_all_instances()

    return stop_app
