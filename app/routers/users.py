from fastapi import APIRouter
from pydantic import BaseModel

from ..database.database import users

router = APIRouter(
    prefix='/users',
    tags=['users']
)


class User(BaseModel):
    name: str
    username: str
    hashed_password: str
    role: str


@router.get('/')
def read_users():
    return users


@router.get('/{username}', response_model=User)
def read_user(username: str):
    return users.get(username)
