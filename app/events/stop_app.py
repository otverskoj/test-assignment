from typing import Callable

from fastapi import FastAPI


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        print('App is shutting down...')

    return stop_app
