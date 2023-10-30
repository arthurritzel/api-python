import mysql.connector

db2 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="4rth1802",
)


def criar_db():
    db2.cursor().execute("create database apiPython")
    db2.cursor().execute("use apiPython")
    db2.cursor().execute("create table pessoas (id int primary key auto_increment, nome varchar(20), idade int)")

criar_db()