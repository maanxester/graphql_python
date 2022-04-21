from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Pessoa, engine, Livro


def create_pessoa(idade: int, nome: str):
    person = Pessoa(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person


def get_pessoas():
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result


def get_livros():
    query = select(Livro).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def create_livros(titulo: str, pessoa_id: int):
    livro = Livro(titulo=titulo, pessoa_id=pessoa_id)

    with Session(engine) as session:
        session.add(livro)
        session.commit()
        session.refresh(livro)

    return livro
