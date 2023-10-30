from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field

from db import *


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='api-python')
spec.register(server)

class QueryPessoa(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    idade: Optional[int]


class Pessoa(BaseModel):
    id: Optional[int]
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list
    count: int


@server.get("/pessoas")
@spec.validate(
    query=QueryPessoa,
    resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """Busca todas as pessoas do banco de dados"""
    query = request.context.query.dict()
    todas_as_pessoas = select_all(query)
    return jsonify(
        Pessoas(
            pessoas=todas_as_pessoas,
            count=len(todas_as_pessoas)
        ).dict()
    )


@server.get("/pessoas/<int:id>")
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoa(id):
    """Busca uma pessoa do banco de dados"""
    try:
        pessoa = select_id(id)
    except IndexError:
        return {"message": "Pessoa nao encontrada"}, 404

    return jsonify(pessoa.__dict__)


@server.post("/pessoas")
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inserir_pessoa():
    """insere uma pessoa no banco de dados"""
    body = request.context.body.dict()
    body["id"] = int(insert(body))
    return body




@server.put("/pessoas/<int:id>")
@spec.validate(
    body=Request(Pessoa), resp=Response(HTTP_201=Pessoa)
)
def altera_pessoa(id):
    """atualiza uma pessoa no banco de dados"""

    body = request.context.body.dict()
    body["id"] = update(body, id)
    return jsonify(body)


@server.delete("/pessoas/<int:id>")
@spec.validate(
    resp=Response("HTTP_204")
)
def deleta_pessoa(id):
    """Deleta uma pessoa no banco de dados"""
    delete(id)
    return jsonify({})



server.run()
