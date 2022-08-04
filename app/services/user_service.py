from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse
from app.storage.repositories.user_repository import IUserRepository


class UserService:
    def __new__(cls, user_repo: IUserRepository):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserService, cls).__new__(cls)
            cls.instance.user_repo = user_repo
        return cls.instance

    def create_user(self, user: UserRequest) -> UserResponse:
        return self.user_repo.create(user)
        
    def get_user_by_id(self, user_id: UUID) -> UserResponse:
        return self.user_repo.get_by_id(user_id)

    def update_user(self, user_id: UUID, user: UserRequest) -> UserResponse:
        return self.user_repo.update(user_id, user)

    def delete_user(self, user_id: UUID) -> None:
        self.user_repo.delete(user_id)
