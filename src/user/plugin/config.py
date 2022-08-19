from typing import Any, Mapping

from pydantic import BaseModel

from src.user.repositories.impl.config import Repository


class UserPluginConfig(BaseModel):
    repository: Repository
