from typing import Union

from pydantic import BaseModel


class PostgresConnectionConfig(BaseModel):
    user: str
    password: str
    name: str
    port: Union[str, int]
    host: str
