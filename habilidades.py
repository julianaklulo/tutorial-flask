from flask import request
from flask_restful import Resource
import json

# Acrescentar na API de habilidade (modulo habilidades) os metodos PUT, POST e DELETE
# O metodo POST devera inserir uma nova habilidade na lista
# O metodo PUT a partir de um ID (identificador da posicao) devera alterar o nome
# da habilidade que esta naquela posicao
# O metodo DELETE devera deletar uma habilidade que esteja na posicao informada na requisicao
# Incluir validaçao no app-restful para verificar se habilidades informadas existem
# na lista_habilidades


lista_habilidades = ['Python', 'Java', 'Flask', 'IoT']


# lista e insere habilidades
class Habilidades(Resource):
    # retorna todas as habilidades
    def get(self):
        return lista_habilidades

    # insere uma habilidade na lista
    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return lista_habilidades[-1]


# edita e deleta habilidades pelo id
class Habilidade(Resource):
    # edita uma habilidade pelo id
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados['habilidade']
        return lista_habilidades[id]

    def delete(self, id):
        lista_habilidades.pop(id)
        response = {'status': 'sucesso', 'mensagem': 'Habilidade excluida!'}
        return response
