from abc import ABC, abstractmethod
from uuid import UUID

from app.user.models.user import User
from app.user.models.user_in_db import UserInDB


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> UserInDB:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> UserInDB:
        pass

    @abstractmethod
    def update(self, user_id: UUID, user: User) -> UserInDB:
        pass
    
    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass
