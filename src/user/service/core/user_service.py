from uuid import UUID
from abc import ABC, abstractmethod

from src.user.models.user import User
from src.user.models.user_in_db import UserInDB


class IUserService(ABC):
    @abstractmethod
    def create_user(self, user: User) -> UserInDB:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> UserInDB:
        pass

    @abstractmethod
    def update_user(self, user_id: UUID, user: User) -> UserInDB:
        pass

    @abstractmethod
    def delete_user(self, user_id: UUID) -> None:
        pass
