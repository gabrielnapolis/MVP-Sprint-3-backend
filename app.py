from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask import request
import jwt, os
from sqlalchemy.exc import IntegrityError

from model import Session, Pessoa, Pokemon
from schemas import *
from flask_cors import CORS
from flask_bcrypt import Bcrypt

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)
bcrypt = Bcrypt(app)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY
# definindo tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)

pessoa_tag = Tag(
    name="Pessoa",
    description="Adição, visualização e remoção de pessoas",
)

pokemon_tag = Tag(
    name="Pokemon",
    description="Adição, visualização e remoção de pokemons",
)


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
    
        
        is_validated = True # validate_email_and_password(data.get('email'), data.get('password'))
        if is_validated is not True:
            return dict(message='Invalid data', data=None, error=is_validated), 400
        session = Session()
        pessoa = session.query(Pessoa).filter(Pessoa.email == data["email"]).first()

        if not pessoa or not bcrypt.check_password_hash(pessoa.senha, str(data["senha"])):
              print(pessoa.senha)
              return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
        else:
            try:
                # token should expire after 24 hrs
                token = jwt.encode(
                    {"id": pessoa.id},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return {
                    "message": "Successfully fetched auth token",
                    "data": token,
                    "id": pessoa.id
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500
        

@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


@app.post(
    "/pessoa",
    tags=[pessoa_tag],
    responses={"200": PessoaViewSchema, "409": ErrorSchema, "400": ErrorSchema},
)
def add_pessoa():
    """Adiciona uma pessoa à base de dados."""
    content: PessoaSchema = request.get_json()

    if "nome" in content and "email" in content:
        if len(content["nome"]) == 0 | len(content["email"]) == 0:
            error_msg = "Nome e Email devem ser preenchidos"
            return {"mesage": error_msg}, 409

        pessoa = Pessoa(
            nome=content["nome"],
            email=content["email"],
            senha=bcrypt.generate_password_hash(content["senha"]).decode('utf-8'),
            idade=content["idade"],
        )

        try:
            session = Session()
            session.add(pessoa)
            session.commit()
            return apresenta_pessoa(pessoa), 200

        except IntegrityError as e:
            error_msg = "Pessoa de mesmo nome já salvo na base"
            return {"mesage": error_msg}, 409

        except Exception as e:
            error_msg = "Não foi possível salvar novo item"
            return {"mesage": error_msg}, 400
    else:
        error_msg = "Nome e Email devem ser preenchidos"
        return {"mesage": error_msg}, 409


@app.get(
    "/pessoas",
    tags=[pessoa_tag],
    responses={"200": ListagemPessoaSchema, "404": ErrorSchema},
)
def get_pessoas():
    """Faz a busca por todas as Pessoas cadastradas""

    Retorna uma representação da listagem de pessoas.
    """
    session = Session()
    pessoas = session.query(Pessoa).all()

    if not pessoas:
        return {"pessoas": []}, 200
    else:
        return apresenta_pessoas(pessoas), 200


@app.route("/pessoa/<pessoa_id>", methods=["GET"])
def get_pessoa(pessoa_id):
    """Faz a busca por uma Pessoa a partir do id"""
    session = Session()
    pessoa = session.query(Pessoa).filter(Pessoa.id == pessoa_id).first()

    if not pessoa:
        error_msg = "Pessoa não encontrada da base"
        return {"mesage": error_msg}, 404
    else:
        return apresenta_pessoa(pessoa), 200


@app.route("/pessoa/<pessoa_id>", methods=["DELETE"])
def del_pessoa(pessoa_id):
    """Deleta uma Pessoa a partir do id informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    session = Session()
    pessoa = session.query(Pessoa).filter(Pessoa.id == pessoa_id).delete()
    session.commit()

    if pessoa:
        return {"mesage": "Pessoa removida", "id": pessoa_id}
    else:
        error_msg = "Pessoa não encontrada na base"
        return {"mesage": error_msg}, 404


@app.route("/pessoa/<pessoa_id>", methods=["PUT"])
def update_pessoa(pessoa_id):
    content: PessoaSchema = request.get_json()
    session = Session()
    pessoa = session.query(Pessoa).filter(Pessoa.id == pessoa_id).first()

    pessoa.nome = content["nome"]
    pessoa.email = content["email"]
    pessoa.idade = content["idade"]

    session.commit()
    if not pessoa:
        error_msg = "Pessoa não encontrada da base"
        return {"mesage": error_msg}, 404
    else:
        return apresenta_pessoa(pessoa), 200


# Crud Pokemon
@app.post(
    "/pokemon",
    responses={"200": PokemonViewSchema, "409": ErrorSchema, "400": ErrorSchema},
)
def add_pokemon():
    """Adiciona uma pessoa à base de dados."""
    content: PokemonSchema = request.get_json()

    if "code" in content and "fk_pessoa" in content:
        pokemon = Pokemon(
            code=content["code"],
            fk_pessoa=content["fk_pessoa"],
        )

        try:
            session = Session()
            session.add(pokemon)
            session.commit()
            return apresenta_pokemon(pokemon), 200

        except IntegrityError as e:
            error_msg = "Pokemon já adicionado para esse treinador"
            return {"mesage": error_msg}, 409

        except Exception as e:
            error_msg = "Não foi possível salvar novo item"
            return {"mesage": error_msg}, 400
    else:
        error_msg = "Campos devem ser preenchidos"
        return {"mesage": error_msg}, 409


@app.get(
    "/pokemon",
    responses={"200": ListagemPokemonSchema, "404": ErrorSchema},
)
def get_pokemons():
    """Faz a busca por todas as Pokemons cadastrados""

    Retorna uma representação da listagem de pokemons.
    """
    session = Session()
    pokemons = session.query(Pokemon).all()

    if not pokemons:
        return {"pokemons": []}, 200
    else:
        return apresenta_pokemons(pokemons), 200


@app.route("/pokemon/<fk_pessoa>", methods=["GET"])
def get_pokemon(fk_pessoa):
    """Faz a busca por Pokemons a partir do Id Pessoa"""
    session = Session()
    pokemon = session.query(Pokemon).filter(Pokemon.fk_pessoa == fk_pessoa).all()

    if not pokemon:
        error_msg = "Nenhum pokemon encontrado para esse treinador"
        return {"mesage": error_msg}, 404
    else:
        return apresenta_pokemons(pokemon), 200

@app.route("/pokemon/<id>", methods=["DELETE"])
def del_pokemon(id):
    """Delete um Pokemon a partir do id informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    session = Session()
    pokemon = session.query(Pokemon).filter(Pokemon.id == id).delete()
    session.commit()

    if pokemon:
        return {"mesage": "Pokemon removido", "id": id}
    else:
        error_msg = "Pokemon não encontrado na base"
        return {"mesage": error_msg}, 404