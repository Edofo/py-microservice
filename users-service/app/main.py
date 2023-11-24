from fastapi import FastAPI
from app.controllers import UsersRouter

app = FastAPI(
    openapi_url="/api/v1/users/openapi.json",
    docs_url="/api/v1/users/docs",
)

app.include_router(UsersRouter, tags=["users"], prefix="/api/v1/users")
