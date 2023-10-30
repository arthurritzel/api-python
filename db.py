import mysql.connector
from app import *
from db_config import db


cursor = db.cursor()

class Pessoa():
    id: int
    nome: str
    idade: int


def select_all(query):
    lista = []
    if query["id"] != None or query["nome"] != None or query["idade"] != None:
        where = "select * from pessoas where "
        if query["id"] != None:
            where += "id = "+str(query["id"])

        if query["nome"] != None:
            if len(where) != 28:
                where += " and "

            where += "nome = '"+str(query["nome"])+"'"
        if query["idade"] != None:
            if len(where) != 28:
                where += " and "

            where += " idade = " + str(query["idade"])
        cursor.execute(where)
    else:
        cursor.execute("select * from pessoas")
    for linha in cursor:
        lista.append(linha)
    db.commit()
    return lista


def select_id(id_banco):
    cursor.execute(("select * from pessoas where id = "+str(id_banco)))
    pessoa = Pessoa()
    for x in cursor:
        pessoa.id = x[0]
        pessoa.nome = x[1]
        pessoa.idade = x[2]

    return pessoa

def insert(body):
    print(body["id"])
    if body["id"] != None and body["id"] != 0:
        cursor.execute("insert into pessoas (id, nome, idade) values (%s, %s, %s)",(body["id"], body["nome"], body["idade"]))
        return body["id"]
    else:
        cursor.execute("insert into pessoas (nome, idade) values (%s, %s)", (body["nome"], body["idade"]))
        cursor.execute("SELECT LAST_INSERT_ID()")
        for x in cursor:
            return x[0]


    db.commit()


def delete(id_banco):
    cursor.execute(("delete from pessoas where id = "+ str(id_banco)))
    db.commit()


def update(body, id_banco):
    if body["id"] != id_banco and body["id"] != 0:
        cursor.execute("UPDATE pessoas SET id = %s, nome = %s, idade = %s WHERE id = %s;", (body["id"], body["nome"], body["idade"], id_banco))
        return body["id"]
    else:
        cursor.execute("UPDATE pessoas SET nome = %s, idade = %s WHERE id = %s;", (body["nome"], body["idade"], id_banco))
        return id_banco
