# Apresentação 

Esse é o MVP, projeto final do 3° módulo da Pós-Graduação em Engenharia de Software da PUC-RIO.

Os requisitos deste projeto eram que fosse desenvolvida uma aplicação, utilizando componentização.

Como mostrado na imagem a seguir, era necessário o desenvolvimento de 03 componentes, sendo eles:

**Componente A:** Desenvolvimento de uma API REST implementada em Python e Flask ou uma interface do usuário, utilizando HTML, CSS e JavaScript com alguma biblioteca ou framework de sua preferência (Angular, React, Vue, etc).

**Componente B:** Uso de uma API externa pública e que ofereça um serviço não pago.

**Componente C:** API REST ou GraphQL. 

Nesse contexto foi utilizado todo o conteúdo apresentado ao longo das matérias de Arquitetura e Projeto de Software, Arquitetura de Microsserviços e Arquitetura de Nuvem e DevOps.

<img src=".\src\assets\img\requisitos.png">

## Para esse projeto, foi utilizada a seguinte arquitetura

**Componente A:** Frontend em Angular.

**Componente B:** PokeApi, API pública onde é possível consultar todos os pokemons, juntamente com seus atributos como: imagens, habilitades, tipos, altura, peso, fraquezas. Documentação: https://pokeapi.co/

**Componente C:** API REST desenvolvida com Python e Flask.

## Sobre este repositório






# Executar a API local

1. Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

    pip install -r requirements.txt

    Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

2. Para executar a API basta executar:

    flask run --host 0.0.0.0 --port 5000 --reload


## Executando através do Docker

# Criar imagem Docker
1. docker build -t backend .

# Executar container
2. docker run -p 5000:5000 backend


