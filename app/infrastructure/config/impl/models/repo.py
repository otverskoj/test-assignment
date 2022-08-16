from typing import Any, Mapping, Optional

from pydantic import BaseModel


class RepositoryConfig(BaseModel):
    type: str
    config: Optional[Mapping[str, Any]] = None

    class Config:
        anystr_strip_whitespace = True
