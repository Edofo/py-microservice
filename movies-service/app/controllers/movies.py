from fastapi import APIRouter, HTTPException
from app.services.movies import MoviesService

router = APIRouter()
moviesService = MoviesService()

@router.get("/")
def getMovies():
    data = moviesService.getMovies()
    return {"data": data}
