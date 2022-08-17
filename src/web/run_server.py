import sys

import click
import uvicorn
from fastapi import FastAPI

from app.infrastructure.config.config import get_application_config
from app.postgres.plugin import PostgresPlugin
from app.user.plugin import UserPlugin


@click.command()
@click.option(
    '--config-path',
    default='/home/oleg/Iqtek/technical-test/configs/application_config.yml',
    help='Path to the config file'
)
def cli(config_path: str) -> None:
    run(config_path)


def run(config_path: str) -> None:
    app = FastAPI()

    config = get_application_config(config_path)

    postgres_plugin = PostgresPlugin()
    postgres_plugin.initialize(config.dict())

    user_plugin = UserPlugin()
    user_plugin.initialize(config.dict())

    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    cli()
