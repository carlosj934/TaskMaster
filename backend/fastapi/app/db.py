from sqlalchemy import create_engine, MetaData
from databases import Database
from config import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)

if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://"))
else:
    engine = create_engine(DATABASE_URL)