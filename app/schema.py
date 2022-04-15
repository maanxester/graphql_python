import strawberry
from typing import Optional
from strawberry.fastapi import GraphQLRouter
from .db_functions import create_pessoa, get_pessoas


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int


@strawberry.type
class Query:
    all_pessoa: list[Pessoa] = strawberry.field(resolver=get_pessoas)


@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_pessoa)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
    )

graphql_app = GraphQLRouter(schema)
