from fastapi import FastAPI
from app.controllers import MoviesRouter

app = FastAPI(
    openapi_url="/api/v1/movies/openapi.json",
    docs_url="/api/v1/movies/docs",
)

app.include_router(MoviesRouter, tags=["movies"], prefix="/api/v1/movies")
