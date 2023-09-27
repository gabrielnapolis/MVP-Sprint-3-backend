from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class Pokemon(Base):
    __tablename__ = "pessoa_pokemons"

    id = Column(Integer, primary_key=True)
    code = Column(Integer, unique=True)
    fk_pessoa = Column (Integer, ForeignKey("pessoa.pessoa_id"), nullable=False)

    def __init__(
        self,
        code: int,
        fk_pessoa: int
    ):
        self.code = code
        self.fk_pessoa = fk_pessoa