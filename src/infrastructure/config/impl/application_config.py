from typing import Any, Mapping

from pydantic import BaseModel


class ServicesConfig(BaseModel):
    user: Mapping[str, Any]


class ApplicationConfig(BaseModel):
    services: ServicesConfig
