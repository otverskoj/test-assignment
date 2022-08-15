import click
import uvicorn
from fastapi import FastAPI

from app.ioc.ioc import ioc
from app.postgres.plugin import PostgresPlugin
from app.user.plugin import UserPlugin
from app.web.plugin import WebPlugin
from app.config.config import get_application_config


@click.command()
@click.option(
    '--config-path',
    default='/home/oleg/Iqtek/technical-test/configs/application_config.yml',
    help='Path to the config file'
)
def main(config_path: str) -> None:
    config = get_application_config(config_path)

    postgres_plugin = PostgresPlugin()
    postgres_plugin.initialize(config.dict())

    user_plugin = UserPlugin()
    user_plugin.initialize(config.dict())

    input()

    # web_plugin = WebPlugin()
    # web_plugin.initialize(config.dict())
    #
    # app = ioc.get_instance(FastAPI)
    #
    # uvicorn.run('main:main', host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
