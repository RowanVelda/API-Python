# - localhost/finanças (get)
# - localhost/finanças (post)
# - localhost/finanças (put)
# - localhost/finanças (delete)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/financeiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

usuarios = [
    {'nome': 'Teste1', 'email': 'teste1@example.com', 'senha': 'senha123'},
    {'nome': 'Teste2', 'email': 'teste2@example.com', 'senha': 'senha456'},
    {'nome': 'Teste3', 'email': 'teste3@example.com', 'senha': 'senha789'},
]

#Consultar usuários
@app.route('/usuarios', methods=['GET'])
def get_users():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados_usuario = request.json
    usuarios.append(dados_usuario)
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201
            
app.run(port=5000, host='localhost', debug=True)