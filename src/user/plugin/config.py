from typing import Any, Mapping

from pydantic import BaseModel


class UserPluginConfig(BaseModel):
    repo_type: str
    repository: Mapping[str, Any]
