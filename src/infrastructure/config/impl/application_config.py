from typing import Any, Mapping

from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    plugins: Mapping[str, Any]
