from pydantic import BaseModel

from app.settings.models.repo import RepositorySettings


class ApplicationSettings(BaseModel):
    repository: RepositorySettings

    class Config:
        anystr_strip_whitespace = True
