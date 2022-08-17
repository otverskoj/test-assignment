from typing import Dict
from uuid import UUID, uuid4

from app.user.models.user import User
from app.user.models.user_in_db import UserInDB
from app.user.repositories.core.user_repository import IUserRepository


class UserInMemoryRepository(IUserRepository):
    __slots__ = ('__storage',)

    def __init__(self) -> None:
        self.__storage: Dict[UUID, UserInDB] = {}

    def create(self, user: User) -> UserInDB:
        user_response = UserInDB(**user.dict(), id_=uuid4())
        self.__storage[user_response.id_] = user_response
        return self.__storage[user_response.id_]

    def get_by_id(self, user_id: UUID) -> UserInDB:
        return self._get_user(user_id)
        
    def update(self, user_id: UUID, user: User) -> UserInDB:
        new_user_data = self._get_user(user_id).dict() | user.dict()
        self.__storage[user_id] = UserInDB(**new_user_data)
        return self.__storage[user_id]
    
    def delete(self, user_id: UUID) -> None:
        self._get_user(user_id)
        del self.__storage[user_id]

    def _get_user(self, user_id: UUID) -> UserInDB:
        if user_id not in self.__storage:
            raise KeyError('User does not exist')
        return self.__storage[user_id]
