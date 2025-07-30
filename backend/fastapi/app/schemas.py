from pydantic import BaseModel, EmailStr
from typing import Optional

class userCreate(BaseModel):
    fullname: str
    email: EmailStr
    username: str
    password: str

class userLogin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    fullname: str
    email: EmailStr
    username: str
    enabled: bool = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] | None = None