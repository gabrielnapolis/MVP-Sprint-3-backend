# Apresentação 

Esse é o MVP, projeto final do 3° módulo da Pós-Graduação em Engenharia de Software da PUC-RIO.

Os requisitos deste projeto eram que fosse desenvolvida uma aplicação, utilizando componentização.

Como mostrado na imagem a seguir, era necessário o desenvolvimento de 03 componentes, sendo eles:

* **Componente A:** Desenvolvimento de uma API REST implementada em Python e Flask ou uma interface do usuário, utilizando HTML, CSS e JavaScript com alguma biblioteca ou framework de sua preferência (Angular, React, Vue, etc).

* **Componente B:** Uso de uma API externa pública e que ofereça um serviço não pago.

* **Componente C:** API REST ou GraphQL. 

Nesse contexto foi utilizado todo o conteúdo apresentado ao longo das matérias de Arquitetura e Projeto de Software, Arquitetura de Microsserviços e Arquitetura de Nuvem e DevOps.

<img src=".\src\assets\img\requisitos.png">

## Para esse projeto, foi utilizada a seguinte arquitetura

* **Componente A:** Frontend em Angular.
Repositório: https://github.com/gabrielnapolis/MVP-Sprint-3-frontend

* **Componente B:** PokeApi, API pública onde é possível consultar todos os pokemons, juntamente com seus atributos como: imagens, habilidades, tipos, altura, peso, fraquezas. Documentação: https://pokeapi.co/

* **Componente C:** API REST desenvolvida com Python e Flask.

# Sobre este repositório

Esse repositório é referente ao Componente C, uma API REST implementada em Python e Flask. Sendo o backend da aplicação, conseguimos realizar o cadastro, edição, leitura e exclusão de treinadores Pokemon e também adicionar e deletar Pokemons aos treinadores. 
A API também conta com uma autenticação de usuário.

Contendo os seguintes endpoints:

* **POST Login** - Realiza a autenticação de usuário;
 
* **POST Pessoa** - Cadastro de usuário;
 
* **GET Pessoas** - Leitura de usuários;
 
* **GET Pessoa** - Leitura de usuário;
 
* **DELETE Pessoa** - Deleta um usuário;
 
* **PUT Pessoa** - Atualização de usuário;
 
* **GET Pessoa/<Id_pessoa>** - Leitura de usuário por ID.
 
* **POST Pokemon** - Adiciona  um pokemon por usuário
 
* **GET Pokemon/<Id_pessoa>** - Leitura de pokemons por ID de usuário.
 
* **DELETE Pokemon** - Deleta um pokemon por ID de usuário.


# Executar projeto via Docker

1° - Criar imagem Docker:

    No diretório raiz do projeto, execute o seguinte comando:

        docker build -t backend .

2° - Executar container

        docker run -p 5000:5000 backend


## Executar a API local

1° - Instalar dependências do projeto:

    Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
    Execute-o da raiz do projeto
    
        pip install -r requirements.txt


2° - Para executar a API basta executar:

        flask run --host 0.0.0.0 --port 5000 --reload




