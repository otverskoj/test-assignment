from typing import Any, Mapping

from pydantic import BaseModel


class ServicesConfig(BaseModel):
    user: Mapping[str, Any]


class ApplicationConfig(BaseModel):
    db_connection: Mapping[str, Any]
    services: ServicesConfig
