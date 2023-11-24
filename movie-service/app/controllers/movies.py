from typing import List
from fastapi import APIRouter, HTTPException

from app.db.models import MovieOut, MovieIn, MovieUpdate
from app.services import movies

movies = APIRouter()

@movies.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not movies.is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_id = await movies.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response

@movies.get('/', response_model=List[MovieOut])
async def get_movies():
    return await movies.get_all_movies()

@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    movie = await movies.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@movies.put('/{id}/', response_model=MovieOut)
async def update_movie(id: int, payload: MovieUpdate):
    movie = await movies.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if 'casts_id' in update_data:
        for cast_id in payload.casts_id:
            if not movies.is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await movies.update_movie(id, updated_movie)

@movies.delete('/{id}/', response_model=None)
async def delete_movie(id: int):
    movie = await movies.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await movies.delete_movie(id)