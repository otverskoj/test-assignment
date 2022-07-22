from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.models.schemas.schemas import UserRequest, UserResponse
from app.errors.user_does_not_exist_error import UserDoesNotExist
from app.services import user_service


router = APIRouter()


@router.get('/users/{user_id}', response_model=UserResponse)
def get_user_by_id(user_id: UUID) -> UserResponse:
    try:
        return user_service.get_user_by_id(user_id)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, 
            detail=f'User with id {user_id} does not exist.'
        )


@router.post('/users/', response_model=UserResponse, status_code=201)
def create_user(user: UserRequest) -> UserResponse:
    return user_service.create_user(user)


@router.put('/users/{user_id}')
def update_user(*, user_id: UUID, user: UserRequest) -> UserResponse:
    try:
        return user_service.update_user(user_id, user)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, 
            detail=f'User with id {user_id} does not exist.'
        )


@router.delete('/users/{user_id}', status_code=204)
def delete_user(user_id: UUID):
    try:
        user_service.delete_user(user_id)
    except UserDoesNotExist:
        raise HTTPException(
            status_code=404, 
            detail=f'User with id {user_id} does not exist.'
        )
