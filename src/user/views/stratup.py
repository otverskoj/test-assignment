from fastapi import FastAPI

from src.infrastructure.ioc.impl.ioc_impl import ioc
from src.user.models.user_in_db import UserInDB
from src.user.service.core.user_service import IUserService
from src.user.views.user_views import UserViews


def user_views_startup() -> None:
    user_service = ioc.get_instance(IUserService)

    user_views = UserViews(user_service)

    app = ioc.get_instance(FastAPI)

    app.add_api_route(
        path='/users/{user_id}',
        endpoint=user_views.get_user_by_id,
        response_model=UserInDB
    )
    app.add_api_route(
        path='/users/',
        endpoint=user_views.create_user,
        response_model=UserInDB,
        status_code=201
    )
    app.add_api_route(
        path='/users/{user_id}',
        endpoint=user_views.update_user,
        response_model=UserInDB
    )
    app.add_api_route(
        path='/users/{user_id}',
        endpoint=user_views.delete_user,
        status_code=204
    )

    ioc.set_instance(FastAPI, app)
