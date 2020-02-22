from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Pessoas, Atividades, Usuarios


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def validação(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                "id": pessoa.id,
                "nome": pessoa.nome,
                "idade": pessoa.idade
            }
        except AttributeError:
            response = {
                "status": "error",
                "mensagem": "Pessoa não encontrada!"
            }
        return response

    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if "nome" in dados:
            pessoa.nome = dados["nome"]
        if "idade" in dados:
            pessoa.idade = dados["idade"]
        pessoa.save()
        response = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }
        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            pessoa.delete()
            response = {
                "status": "success",
                "mensagem": f"Pessoa {pessoa.nome} deletada com sucesso!"
            }
        except AttributeError:
            response = {
                "status": "error",
                "mensagem": "Pessoa não encontrada!"
            }
        return response


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id": i.id, "nome": i.nome, "idade": i.idade} for i in pessoas]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados["nome"], idade=dados["idade"])
        pessoa.save()
        response = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome, "status": i.status} for i in atividades]

        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
        atividade = Atividades(nome=dados["nome"], pessoa=pessoa)
        atividade.save()
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.nome,
            "status": atividade.status
        }
        return response


class ListaAtividadesPessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        atividades = Atividades.query.filter_by(pessoa=pessoa)
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome, "status": i.status} for i in atividades]
        return response


class Atividade(Resource):
    def get(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.nome,
            "status": atividade.status
        }
        return response

    @auth.login_required
    def put(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        dados = request.json
        if "status" in dados:
            status = dados["status"]
            if status == "pendente":
                atividade.status = False
            elif status == "concluído":
                atividade.status = True
        atividade.save()
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.nome,
            "status": atividade.status
        }
        return response


api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListaPessoas, "/pessoa/")
api.add_resource(ListaAtividades, "/atividade/")
api.add_resource(ListaAtividadesPessoa, "/atividade/<string:nome>/")
api.add_resource(Atividade, "/atividade/<int:id>/")


if __name__ == "__main__":
    app.run(debug=True)
