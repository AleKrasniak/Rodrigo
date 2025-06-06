import tkinter as tk
from tkinter import messagebox
import mysql.connector


class ClienteDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="busquestudios2"
        )
        self.cursor = self.conexao.cursor()

    def criar(self, cliente):
        sql = "INSERT INTO cliente (id_perfil, id_endereco, nome, dt_nasc, genero, telefone, cpf, email, login, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (cliente.id_perfil, cliente.id_endereco, cliente.nome, cliente.dt_nasc, cliente.genero, cliente.telefone, cliente.cpf, cliente.email, cliente.login, cliente.senha))
        self.conexao.commit()

    def listar(self):
        self.cursor.execute ("SELECT * FROM cliente")
        return self.cursor.fetchall()
    
    def atualizar(self, cliente):
        sql = "UPDATE cliente SET id_perfil = %s, id_endereco = %s, nome= %s, dt_nasc, genero = %s, telefone = %s, cpf = %s, email = %s, login =%s, senha =%s WHERE id_cliente = %s"
        self.cursor.execute(sql, (cliente.id_perfil, cliente.id_endereco, cliente.nome, cliente.dt_nasc, cliente.genero, cliente.telefone, cliente.cpf, cliente.email, cliente.login, cliente.senha, cliente.id_cliente))
        self.conexao.commit

    def deletar(self, id_cliente):
        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        self.cursor.execure(sql,(id_cliente,))
        self.conexao.commit()




# def __init__(self, id_cliente=None, id_perfil=None, id_endereco=None, nome="", dt_nasc="", genero="", telefone="", cpf="", email="", login="", senha=""):
#         self.id_cliente = id_cliente
#         self.id_perfil = id_perfil
#         self.id_endereco = id_endereco
#         self.nome = nome
#         self.dt_nasc = dt_nasc
#         self.genero = genero
#         self.telefone = telefone 
#         self.cpf = cpf 
#         self.email = email
#         self.login = login
#         self.senha = senha