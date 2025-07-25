from pydantic import BaseModel, EmailStr

class userCreate(BaseModel):
    fullname: str
    email: EmailStr
    username: str
    password: str

class userLogin(BaseModel):
    username: str
    password: str