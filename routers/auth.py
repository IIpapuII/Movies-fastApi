from fastapi import APIRouter
from schema.movie import  User
from controller.jwt_manager import create_token

auth_router = APIRouter()

@auth_router.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return token