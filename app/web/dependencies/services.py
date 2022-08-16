from app.infrastructure.ioc.impl.ioc_impl import ioc
from app.user.service.core.user_service import IUserService
from app.user.service.impl.user_service_impl import UserServiceImpl


def get_user_service() -> UserServiceImpl:
    return ioc.get_instance(IUserService)
