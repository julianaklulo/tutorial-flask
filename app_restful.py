from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {'id': 0,
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},

    {'id': 1,
     'nome': 'Juliana',
     'habilidades': ['Python', 'IoT']}
]


# devolve um desenvolvedor pelo id, tambem altera e deleta
class Desenvolvedor(Resource):
    # pega o registro pelo id
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolver de id {} nao existe!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido! Procure a documentaçao'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    # altera o registro pelo id
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        response = dados
        return response

    # deleta o registro pelo id
    def delete(self, id):
        desenvolvedores.pop(id)
        response = {'status': 'sucesso', 'mensagem': 'registro excluido'}
        return response


# lista todos os desenvolvedores e permite inserir
class ListaDesenvolvedores(Resource):
    # retorna todos os registros
    def get(self):
        return desenvolvedores

    # insere o registro
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
