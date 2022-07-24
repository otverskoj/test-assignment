from fastapi import FastAPI
from app.api.routers import users
from app.events.events import shutdown_app


app = FastAPI(
    on_shutdown=[shutdown_app]
)


app.include_router(users.router)


@app.get("/")
def root():
    return {
        "message": "Hello, Iqtek!"
    }
