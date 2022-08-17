from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    middle_name: str = Field(max_length=100)
