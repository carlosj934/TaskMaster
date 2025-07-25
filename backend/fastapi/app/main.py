from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from db import database, metadata, engine
from models import users
from schemas import userCreate, userLogin

app = FastAPI()
metadata.create_all(engine)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/auth/register")
async def register(user: userCreate):
    query = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists.")
    query = users.select().where(users.c.email == user.email)
    existing_email = await database.fetch_one(query)
    if existing_email:
        raise HTTPException(status_code=400, detail="User already registered with this email.")
    hashed_password = pwd_context.hash(user.password)
    query = users.insert().values(fullname=user.fullname, email=user.email, username=user.username, password=hashed_password)
    await database.execute(query)
    return {"message": "User registered successfully"}

@app.post("/auth/login")
async def login(user: userLogin):
    query = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(query)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login succesful"}
