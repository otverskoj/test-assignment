import click
import uvicorn

from src.entrypoints.fastapi import entrypoint


@click.command()
@click.option(
    '--config-path',
    default='configs/application_config.yml',
    help='Path to the config file'
)
def main(config_path: str) -> None:
    app = entrypoint.get_app(config_path)
    uvicorn.run(app, port=8000, host='0.0.0.0')


if __name__ == '__main__':
    main()
