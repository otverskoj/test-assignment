# from fastapi import FastAPI
# from app.web.api.routers import users
# from app.web.events.start_app import create_start_app_handler
# from app.web.events.stop_app import create_stop_app_handler
# from app.config.config import get_application_config
#
#
# def get_application() -> FastAPI:
#     settings = get_application_config()
#
#     app = FastAPI()
#
#     app.include_router(users.router)
#
#     app.add_event_handler(
#         "startup",
#         create_start_app_handler(settings),
#     )
#     app.add_event_handler(
#         "shutdown",
#         create_stop_app_handler(app),
#     )
#
#     return app
#
#
# app = get_application()
