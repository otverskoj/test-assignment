from typing import Optional, Mapping, Any

from pydantic import BaseModel


class Repository(BaseModel):
    settings: Optional[Mapping[str, Any]] = None
