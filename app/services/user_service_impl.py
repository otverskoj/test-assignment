from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse
from app.services.user_service import IUserService
from app.storage.repositories.user_repository import IUserRepository


class UserServiceImpl(IUserService):
    # def __new__(cls, user_repo: IUserRepository):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(UserServiceImpl, cls).__new__(cls)
    #         cls.instance.user_repo = user_repo
    #     return cls.instance

    __slots__ = ('__user_repo',)

    def __init__(self, user_repo: IUserRepository) -> None:
        self.__user_repo = user_repo

    def create_user(self, user: UserRequest) -> UserResponse:
        return self.__user_repo.create(user)
        
    def get_user_by_id(self, user_id: UUID) -> UserResponse:
        return self.__user_repo.get_by_id(user_id)

    def update_user(self, user_id: UUID, user: UserRequest) -> UserResponse:
        return self.__user_repo.update(user_id, user)

    def delete_user(self, user_id: UUID) -> None:
        self.__user_repo.delete(user_id)
