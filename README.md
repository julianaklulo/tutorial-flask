# API REST para gerenciamento de Atividades
API criada durante curso Desenvolvimento avançado Python com Flask e REST API na plataforma Digital Innovation One

### Instruções
Inicializar o ambiente virtual: `pipenv shell`

Instalar as dependências: `pipenv install`

Criar o usuário para as rotas autenticadas no arquivo `utils.py`

#### Rotas

Listar todas as pessoas: `GET em http://127.0.0.1:5000/pessoa/`

Adicionar nova pessoa: `POST em http://127.0.0.1:5000/pessoa/` com os dados (nome, idade)

Exibir dados de uma pessoa: `GET em http://127.0.0.1:5000/pessoa/<nome_da_pessoa>/`

Alterar dados de uma pessoa: `PUT em http://127.0.0.1:5000/pessoa/<nome_da_pessoa>/` com os dados (nome, idade)

Deletar uma pessoa: `DELETE em http://127.0.0.1:5000/pessoa/<nome_da_pessoa>/`

Listar todas as atividades: `GET em http://127.0.0.1:5000/atividade/`

Adicionar nova atividade: `POST em http://127.0.0.1:5000/atividade/` com os dados (nome, pessoa[nome], status[pendente/concluído])

Listar todas as atividades de uma pessoa: `GET em http://127.0.0.1:5000/atividade/<nome_da_pessoa>/`

Listar uma atividade: `GET em http://127.0.0.1:5000/atividade/<id_da_atividade>/`

Alterar o status de uma atividade: `PUT em http://127.0.0.1:5000/atividade/<id_da_atividade>/`com os dados (status[pendente/concluído])
