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

app.run()
