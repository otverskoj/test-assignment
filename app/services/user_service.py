from uuid import UUID
from abc import ABC, abstractmethod

from app.models.schemas.schemas import UserRequest, UserResponse


class IUserService(ABC):
    @abstractmethod
    def create_user(self, user: UserRequest) -> UserResponse:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> UserResponse:
        pass

    @abstractmethod
    def update_user(self, user_id: UUID, user: UserRequest) -> UserResponse:
        pass

    @abstractmethod
    def delete_user(self, user_id: UUID) -> None:
        pass
