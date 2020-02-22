from models import Pessoas, Atividades, Usuarios


def insere_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()


def consulta_pessoas(nome):
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    print(pessoa.idade)


def altera_pessoas(nome, idade):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.idade = idade
    pessoa.save()


def exclui_pessoas(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.delete()


def exclui_atividades():
    atividades = Atividades.query.all()
    for a in atividades:
        a.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


if __name__ == "__main__":
    insere_pessoas("Juliana", 23)
    insere_pessoas("Karoline", 24)
    insere_usuario("admin", "admin")
