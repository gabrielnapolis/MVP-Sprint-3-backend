from pydantic import BaseModel
from typing import List
from model.pokemon import Pokemon

class PokemonSchema(BaseModel):
    id: int = 1
    code: int = 1
    fk_pessoa: int = 1

class PokemonBuscaSchema(BaseModel):
    id: int = 1

class ListagemPokemonSchema(BaseModel):
    pokemons: List[PokemonSchema]

def apresenta_pokemons(pokemons: List[Pokemon]):
    result = []

    for pokemon in pokemons:
        result.append(
            {
                "id": pokemon.id,
                "code": pokemon.code,
                "fk_pessoa": pokemon.fk_pessoa
            },
        )
    return {"pokemons": result}

class PokemonViewSchema(BaseModel):
    id: int = 1
    code: int = 1
    fk_pessoa: int = 1

class PokemonDelSchema(BaseModel):
    masage: str
    code: str

def apresenta_pokemon(pokemon: Pokemon):
    return {
        "id": pokemon.id,
        "code": pokemon.code,
        "fk_pessoa": pokemon.fk_pessoa
    }