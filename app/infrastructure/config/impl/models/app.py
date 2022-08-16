from typing import List

from pydantic import BaseModel

from ..models.repo import RepositoryConfig


class ApplicationConfig(BaseModel):
    repository: RepositoryConfig

    class Config:
        anystr_strip_whitespace = True
