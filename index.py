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
            return {"algo deu errado":"usuario ja cadastrado"}
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
        if login[""]




app.run()
    
    