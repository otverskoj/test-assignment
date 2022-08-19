from typing import Mapping, Any, Optional

from pydantic import BaseModel


class DBConnectionCreatorPluginConfig(BaseModel):
    type: str
    settings: Optional[Mapping[str, Any]] = None
