from sqlmodel import SQLModel, create_engine

from decouple import config

engine = create_engine(config("DB_URL"), connect_args={
    "check_same_thread": False
})

def create_database():
    SQLModel.metadata.create_all(engine)