from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import select
from model import Base

class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column("pessoa_id", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    email = Column(String(140))
    senha = Column(String(140))
    idade = Column(Integer)

    #pokemons = relationship("pessoa_pokemons")
    
    def __init__(
        self,
        nome: str,
        email: str,
        senha: str,
        idade: int,
    ):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade
        