from typing import List, Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    name: str
    phone: str
    email: str
    roles: List[str] = []

class UserCreate(UserBase):

    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class LoginUser():
    email: str
    password: str
