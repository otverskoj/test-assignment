from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.models.schemas.schemas import UserRequest, UserResponse
from app.errors.user_does_not_exist_error import UserDoesNotExist
from app.errors.db_cant_handle_query_error import DBCantHandleQuery
from app.services.user_service import IUserService
from app.api.dependencies.services import get_user_service


router = InferringRouter()


@cbv(router)
class UserCBV:
    user_service: IUserService = Depends(get_user_service)

    @router.get('/users/{user_id}', response_model=UserResponse)
    def get_user_by_id(
        self,
        user_id: UUID
    ) -> UserResponse:
        try:
            return self.user_service.get_user_by_id(user_id)
        except UserDoesNotExist:
            raise HTTPException(
                status_code=404,
                detail=f'User with id {user_id} does not exist.'
            )
        except DBCantHandleQuery as err:
            raise HTTPException(
                status_code=404,
                detail=f"DB can't handle query: {str(err)}"
            )

    @router.post('/users/', response_model=UserResponse, status_code=201)
    def create_user(
        self,
        user: UserRequest
    ) -> UserResponse:
        try:
            return self.user_service.create_user(user)
        except DBCantHandleQuery as err:
            raise HTTPException(
                status_code=404,
                detail=f"DB can't handle query: {str(err)}"
            )

    @router.put('/users/{user_id}')
    def update_user(
        self,
        user_id: UUID,
        user: UserRequest,
    ) -> UserResponse:
        try:
            return self.user_service.update_user(user_id, user)
        except UserDoesNotExist:
            raise HTTPException(
                status_code=404,
                detail=f'User with id {user_id} does not exist.'
            )
        except DBCantHandleQuery as err:
            raise HTTPException(
                status_code=404,
                detail=f"DB can't handle query: {str(err)}"
            )

    @router.delete('/users/{user_id}', status_code=204)
    def delete_user(
        self,
        user_id: UUID
    ):
        try:
            self.user_service.delete_user(user_id)
        except UserDoesNotExist:
            raise HTTPException(
                status_code=404,
                detail=f'User with id {user_id} does not exist.'
            )
        except DBCantHandleQuery as err:
            raise HTTPException(
                status_code=404,
                detail=f"DB can't handle query: {str(err)}"
            )
