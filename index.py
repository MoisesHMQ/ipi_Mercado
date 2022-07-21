from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

usuarios = []
produtos = []


@app.route("/cadastrar/usuarios", methods=['POST'])
def cadastrar():
    body = request.json 
    for user in usuarios:
        if user["email"] == body["email"]:  
            return {"Algo deu errado.":"Esse usuario ja existe."}
    body = {
        "id": str(uuid.uuid4()),
        "email": body["email"],
        "senha": body["senha"]
        }
    usuarios.append(body)
    return jsonify(body)

@app.route("/login", methods=['POST'])
def logar():
    body_login = request.json
    for login in usuarios:
        if login["email"] == body_login["email"] and login["senha"] == body_login["senha"]:
            return{"Status":"Logado."}
        else:
            return{"Status":"Usuario ou Senha Incorretos."}

@app.route("/carrinho/produtos", methods=['POST'])
def Frutas():
    produto_mercado = request.json 
    for produto_mercado in produtos:
        if produto_mercado["produtos"] == produto_mercado["produtos"]: 
            return {"status":"Produto já cadastrado."}
    produto_mercado = {
        "id": str(uuid.uuid4()),
        "produtos": produto_mercado["produtos"]
        }
    produtos.append(produto_mercado)
    return jsonify(produto_mercado)


@app.route("/listar/usuarios")
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/listar/produtos")
def listar_produtos():
    return jsonify(produtos)


@app.route("/excluir/usuarios", methods=['POST'])
def excluir_usuarios():
    body_excluir = request.json
    print(usuarios)
    for list in usuarios:
        if list["id"] == body_excluir["id"]:
            usuarios.remove(list)
            return body_excluir

@app.route("/excluir/produtos", methods=['POST'])
def excluir_produtos():
    body_excluir = request.json
    print(produtos)
    for list1 in produtos:
        if list1["id"] == body_excluir["id"]:
            produtos.remove(list1)
            return body_excluir
app.run()
