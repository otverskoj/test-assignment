from typing import Dict
from uuid import UUID, uuid4

from src.user.models.user import User
from src.user.models.user_in_db import UserInDB
from src.user.repositories.core.exceptions import UserDoesNotExist
from src.user.repositories.core.user_repository import IUserRepository


class UserInMemoryRepository(IUserRepository):
    __slots__ = ('__storage',)

    def __init__(self) -> None:
        self.__storage: Dict[UUID, UserInDB] = {}

    def create(self, user: User) -> UserInDB:
        unique_id = self.__create_unique_id()
        user_response = UserInDB(**user.dict(), id_=unique_id)
        self.__storage[user_response.id_] = user_response
        return self.__storage[user_response.id_]

    def get_by_id(self, user_id: UUID) -> UserInDB:
        return self.__get_user(user_id)
        
    def update(self, user_id: UUID, user: User) -> UserInDB:
        user_to_update = self.__get_user(user_id).dict()
        user_to_update.update(user.dict())
        self.__storage[user_id] = UserInDB(**user_to_update)
        return self.__storage[user_id]
    
    def delete(self, user_id: UUID) -> None:
        self.__get_user(user_id)
        del self.__storage[user_id]

    def __create_unique_id(self) -> UUID:
        return uuid4()

    def __get_user(self, user_id: UUID) -> UserInDB:
        if user_id in self.__storage:
            return self.__storage[user_id]
        raise UserDoesNotExist()
