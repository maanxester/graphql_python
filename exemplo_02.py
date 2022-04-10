import strawberry
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


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int


# Create Database
SQLModel.metadata.create_all(engine)


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int


@strawberry.type
class Query:
    @strawberry.field
    def all_pessoa(self) -> list[Pessoa]:
        query = select(Person)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()
        return result


schema = strawberry.Schema(query=Query)

