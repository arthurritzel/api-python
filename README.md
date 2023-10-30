# Readme do Repositório da API em Python

Este repositório contém uma API desenvolvida em Python usando as bibliotecas Flask, SQL e Pydantic. A API foi projetada para fornecer uma interface simples e eficaz para realizar operações de CRUD (Create, Read, Update, Delete) em um banco de dados. Este README fornece informações essenciais sobre como configurar, executar e usar a API.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha as seguintes dependências instaladas:

- Python 3.x
- Flask
- Pydantic
- MySQL

## Instalação

1. Clone este repositório em seu ambiente de desenvolvimento:

```
git clone https://github.com/seu-usuario/repositorio-api-python.git
```

2. Navegue até o diretório do projeto:

```
cd repositorio-api-python
```

3. Crie e ative um ambiente virtual (recomendado):

```
python -m venv venv
source venv/bin/activate  # No Windows, utilize venv\Scripts\activate
```

4. Instale as dependências do projeto:


5. Configuração do Banco de Dados:

    - Edite o arquivo `db_config.py` para configurar as credenciais do banco de dados de acordo com suas necessidades.

6. Criando Banco de Dados:

    - Execute a função de criação do banco de dados para criar as tabelas necessárias:

```
python3 criar_db.py criar_db
```

7. Inicie a API:

```
flask run
```

A API agora deve estar em execução e acessível em `http://localhost:5000`..

## Uso da API

A API oferece rotas para realizar operações de CRUD em recursos. Certifique-se de verificar a documentação da API para obter informações detalhadas sobre como usar cada rota.

## Documentação

A documentação da API está disponível em `http://localhost:5000/docs/swagger`. A documentação é gerada automaticamente usando Swagger/OpenAPI e fornece detalhes sobre as rotas, parâmetros e exemplos de solicitação/resposta.
