from flask import Flask, jsonify, request
import json


app = Flask(__name__)


desenvolvedores = [
    {'id': 0,
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},

    {'id': 1,
     'nome': 'Juliana',
     'habilidades': ['Python', 'IoT']}
]


# devolve um desenvolvedor pelo id, tambem altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    # pega o registro pelo id
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolver de id {} nao existe!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido! Procure a documentaçao'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    # altera o registro
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    # deleta o registro
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem':'registro excluido'})


# lista todos os desenvolvedores e permite inserir
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    # insere o registro
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    # retorna todos os registros
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
