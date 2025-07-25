from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
import requests


class userRegister(BaseModel):
    fullName: str
    userName: str
    email: EmailStr
    password: str

class userLogin(BaseModel):
    userName: str
    password: str

app = FastAPI()

@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def userRegister(userregister: userRegister):
    pass

@app.post("/auth/login", status_code=status.HTTP_201_CREATED)
async def userLogin(userlogin: userLogin):
    pass

