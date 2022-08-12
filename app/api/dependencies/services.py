from app.ioc.ioc import ioc
from app.services.user_service import IUserService
from app.services.user_service_impl import UserServiceImpl


def get_user_service() -> UserServiceImpl:
    return ioc.get_instance(IUserService)
