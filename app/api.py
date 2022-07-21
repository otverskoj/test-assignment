from uuid import UUID

from fastapi import FastAPI, HTTPException

from app.schemas import UserRequest, UserResponse
from app.repositories import get_user_repository
from app.exceptions import UserDoesNotExist


app = FastAPI()


@app.get('/users/{user_id}', response_model=UserResponse)
def get_user_by_id(user_id: UUID) -> UserResponse:
    try:
        return get_user_repository().get_by_id(user_id)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, detail=f'User with id {user_id} does not exist.'
        )


@app.post('/users/', response_model=UserResponse, status_code=201)
def create_user(user: UserRequest) -> UserResponse:
    return get_user_repository().create(user)


@app.put('/users/{user_id}')
def update_user(*, user_id: UUID, user: UserRequest) -> UserResponse:
    try:
        return get_user_repository().update(user_id, user)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, detail=f'User with id {user_id} does not exist.'
        )


@app.delete('/users/{user_id}', status_code=204)
def delete_user(user_id: UUID):
    try:
        get_user_repository().delete(user_id)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, detail=f'User with id {user_id} does not exist.'
        )
