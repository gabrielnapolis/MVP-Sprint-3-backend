from pydantic import BaseModel
from typing import List
from model.pessoa import Pessoa


class PessoaSchema(BaseModel):
    id: int = 1
    nome: str = "Nome"
    email: str = "email@email.com"
    senha: str = "senha"
    idade: int = 27


class PessoaBuscaSchema(BaseModel):
    id: int = 1


class ListagemPessoaSchema(BaseModel):
    pessoas: List[PessoaSchema]


def apresenta_pessoas(pessoas: List[Pessoa]):
    result = []

    for pessoa in pessoas:
        result.append(
            {
                "id": pessoa.id,
                "nome": pessoa.nome,
                "email": pessoa.email,
                "senha": pessoa.senha,
                "idade": pessoa.idade,
            },
        )

    return {"pessoas": result}


class PessoaViewSchema(BaseModel):
    id: int = 1
    nome: str = "Nome"
    email: str = "email@email.com"
    idade: int = 20


class PessoaDelSchema(BaseModel):
    mesage: str
    nome: str


def apresenta_pessoa(pessoa: Pessoa):
    return {
        "id": pessoa.id,
        "nome": pessoa.nome,
        "email": pessoa.email,
        "idade": pessoa.idade
    }
