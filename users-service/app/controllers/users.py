from fastapi import APIRouter, HTTPException
from app.services.users import UsersService

router = APIRouter()
usersService = UsersService()

@router.get("/")
def getUsers():
    data = usersService.getUsers()
    return {"data": data}
