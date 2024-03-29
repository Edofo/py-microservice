from fastapi import APIRouter, HTTPException

from app.db.models import CastOut, CastIn
from app.services import casts

casts = APIRouter()

@casts.post('/', response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn):
    cast_id = await casts.add_cast(payload)

    response = {
        'id': cast_id,
        **payload.dict()
    }

    return response

@casts.get('/{id}/', response_model=CastOut)
async def get_cast(id: int):
    cast = await casts.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast