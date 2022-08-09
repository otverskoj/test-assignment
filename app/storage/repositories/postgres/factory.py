from typing import Optional, Mapping, Any

from pydantic import ValidationError

from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.postgres.settings_model import UserPostgresRepositorySettings
from app.storage.repositories.postgres.repository import UserPostgresRepository
from app.storage.repositories.postgres.connection_creator import PostgresConnectionCreator
from app.errors.cant_validate_repository_settings import CantValidateRepositorySettings
from app.settings.setting_models.app import ApplicationSettings


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    def get_user_repository(
        self,
        settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        try:
            repo_settings = UserPostgresRepositorySettings(**settings.dict())
        except ValidationError:
            raise CantValidateRepositorySettings

        connection = PostgresConnectionCreator(repo_settings).connection

        return UserPostgresRepository(connection)
