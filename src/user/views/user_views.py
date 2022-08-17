from uuid import UUID

from src.user.models.user import User
from src.user.models.user_in_db import UserInDB
from src.user.service.core.user_service import IUserService


class UserViews:
    __slots__ = ('__service',)

    def __init__(self, service: IUserService) -> None:
        self.__service = service

    def get_user_by_id(
        self,
        user_id: UUID
    ) -> UserInDB:
        return self.__service.get_user_by_id(user_id)

    def create_user(
        self,
        user: User
    ) -> UserInDB:
        return self.__service.create_user(user)

    def update_user(
        self,
        user_id: UUID,
        user: User,
    ) -> UserInDB:
        return self.__service.update_user(user_id, user)

    def delete_user(
        self,
        user_id: UUID
    ):
        self.__service.delete_user(user_id)
