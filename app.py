from flask import Flask, jsonify, request

#iniciando o Flask
app = Flask(__name__)

# Definido uma biblioteca para ser a base de dados teste
produtos = [
    {
        'id': 1,
        'nome': 'descanso de tela',
        'preco': 30
    },
    {
        'id': 2,
        'nome': 'teclado',
        'preco': 30
    },
    {
        'id': 3,
        'nome': 'mouse',
        'preco': 35
    },
    {
        'id': 4,
        'nome': 'monitor ultraeide',
        'preco': 1500
    },
    {
        'id': 5,
        'nome': 'placa de vídeo',
        'preco': 2500
    }
]

# -----------------------Definindo rotas e métodos -----------------------------------------------------------------
# Consultar (todos)
@app.route('/produtos',methods=['GET'])
def obter_produtos():
    return jsonify(produtos)

# Consultar por (id)
@app.route('/produtos/<int:id>',methods=['GET'])
def obter_produto_por_id(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)

# Editar por id
@app.route('/produtos/<int:id>',methods=['PUT'])
def editar_produto_por_id(id):
    produto_alterado = request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])

# Criar
@app.route('/produtos',methods=['POST'])
def incluir_novo_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    
    return jsonify(produtos)

# Excluir por id
@app.route('/produtos/<int:id>',methods=['DELETE'])
def excluir_produto(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)

# Iniciando o programa e já definido a porta e localhost-----------------------
app.run(port=5000,host='localhost',debug=True)