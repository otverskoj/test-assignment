from pydantic import BaseModel

from src.user.repositories.impl.config import Repository


class UserConfig(BaseModel):
    repository: Repository
