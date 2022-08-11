from typing import Any, Mapping, Optional

from pydantic import BaseModel


class RepositorySettings(BaseModel):
    type: str
    settings: Optional[Mapping[str, Any]] = None

    class Config:
        anystr_strip_whitespace = True
