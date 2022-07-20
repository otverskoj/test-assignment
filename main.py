from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel, Field


app = FastAPI()


class User(BaseModel):
    id: Optional[int] = Field(default=None, ge=0)
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    middle_name: Optional[str] = Field(default=None, max_length=100)


@app.get('/users/{user_id}', response_model=User)
def get_user(user_id: int = Path(ge=0)) -> User:
    return user


@app.post('/users/', response_model=User, status_code=201)
def create_user(user: User) -> User:
    return user


@app.put('/users/{user_id}')
def update_user(*, user_id: int = Path(ge=0), user: User):
    pass


@app.delete('/users/{user_id}', status_code=204)
def delete_user(user_id: int = Path(ge=0)):
    pass
