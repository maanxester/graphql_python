from typing import Optional
from fastapi import FastAPI
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    select,
    Session,
)

# Create Engine
engine = create_engine('sqlite:///database.db')

# Create App
app = FastAPI()


class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int


# Create Database
SQLModel.metadata.create_all(engine)


@app.get("/")
def home():
    return {"message": "ok"}


@app.get("/pessoa")
def get_pessoa():
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result

