from uuid import UUID

from src.user.service.core.user_service import IUserService
from src.user.views.models.request import UserRequest
from src.user.views.models.response import UserResponse


__all__ = [
    'UserViews'
]


class UserViews:
    __slots__ = ('__service',)

    def __init__(self, service: IUserService) -> None:
        self.__service = service

    def get_user_by_id(
        self,
        user_id: UUID
    ) -> UserResponse:
        user_in_db = self.__service.get_user_by_id(user_id)
        return UserResponse(**user_in_db.dict())

    def create_user(
        self,
        user: UserRequest
    ) -> UserResponse:
        user_in_db = self.__service.create_user(user)
        return UserResponse(**user_in_db.dict())

    def update_user(
        self,
        user_id: UUID,
        user: UserRequest,
    ) -> UserResponse:
        user_in_db = self.__service.update_user(user_id, user)
        return UserResponse(**user_in_db.dict())

    def delete_user(
        self,
        user_id: UUID
    ):
        self.__service.delete_user(user_id)
