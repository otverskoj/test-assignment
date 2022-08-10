from fastapi import Depends

from app.services.user_service import UserService
from app.storage.repositories.user_repository import IUserRepository
from app.api.dependencies.repositories import get_user_repository


def get_user_service(
    user_repo: IUserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repo)
