from app.settings import REPOSITORY_TYPE
from app.storage.base_repository import repository


def shutdown_app() -> None:
    if REPOSITORY_TYPE == 'db':
        repository.close_connection()
    else:
        print('Shutdown!')
