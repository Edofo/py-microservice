from app.db.models import MovieIn
from app.db.db import movies, database

import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/casts/'

def is_cast_present(cast_id: int):
    url = os.environ.get('CAST_SERVICE_HOST_URL') or CAST_SERVICE_HOST_URL
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False

async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_movies():
    query = movies.select()
    return await database.fetch_all(query=query)

async def get_movie(id):
    query = movies.select(movies.c.id==id)
    return await database.fetch_one(query=query)

async def delete_movie(id: int):
    query = movies.delete().where(movies.c.id==id)
    return await database.execute(query=query)

async def update_movie(id: int, payload: MovieIn):
    query = (
        movies
        .update()
        .where(movies.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
