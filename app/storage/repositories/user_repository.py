from abc import ABC, abstractmethod
from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: UserRequest) -> UserResponse:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> UserResponse:
        pass

    @abstractmethod
    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        pass
    
    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass
