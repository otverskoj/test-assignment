from typing import Optional, Mapping, Any

from pydantic import BaseSettings



class RepositorySettings(BaseSettings):
    type: str
    settings: Optional[Mapping[str, Any]] = None

    class Config:
        anystr_strip_whitespace = True


class ApplicationSettings(BaseSettings):
    repository: RepositorySettings

    class Config:
        anystr_strip_whitespace = True
