from sqlalchemy import Table, Column, Integer, String
from db import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fullname", String(100), unique=False, nullable=False, index=True),
    Column("email", String(100), unique=True, nullable=False, index=True),
    Column("username", String(50), unique=True, nullable=False, index=True),
    Column("password", String)
)