from typing import Optional, Mapping, Any

from pydantic import ValidationError

from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.user_repository import IUserRepository
from app.storage.repositories.postgres.settings_model import UserPostgresRepositorySettings
from app.storage.repositories.postgres.repository import UserPostgresRepository
from app.storage.repositories.postgres.connection_creator import PostgresConnectionCreator
from app.errors.cant_validate_repository_settings import CantValidateRepositorySettings


class UserPostgresRepositoryFactory(IUserRepositoryFactory):
    __repo_type = 'postgres'

    @classmethod
    def repo_type(cls) -> str:
        return cls.__repo_type

    def get_user_repository(
        self,
        repo_settings: Optional[Mapping[str, Any]] = None
    ) -> IUserRepository:
        try:
            settings = UserPostgresRepositorySettings(**repo_settings)
        except ValidationError:
            raise CantValidateRepositorySettings

        connection = PostgresConnectionCreator(settings).connection

        return UserPostgresRepository(connection)
