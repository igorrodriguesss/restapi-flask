# restapi-flask

# 🐍 REST API com Flask & MongoDB

Este projeto é uma API REST construída com **Flask**, persistindo dados em **MongoDB**, e preparada para deploy utilizando **Docker** e **Render**. Cobre configurações de testes, linting e pipeline CI/CD com **GitHub Actions**.

## 🔧 Tecnologias

- Linguagem: **Python 3.9+**
- Framework web: **Flask**
- Banco de dados: **MongoDB**
- Testes: **pytest**
- Linting/Formatação: **flake8**, **make flake**
- Integração contínua: **GitHub Actions**
- Deploy local: **Docker Compose**
- Deploy remoto: **Render** (opcionalmente configurável manualmente via hooks)

## 🚀 Como rodar localmente

### Pré-requisitos

- Python ≥ 3.9
- Docker & Docker Compose (opcional, mas recomendado)
- MongoDB (local ou via Docker)
- (Opcional) `.env` com variáveis como `MONGO_URI`, `FLASK_ENV`, etc.

### 🔁 Opção A: com Docker Compose

```bash
docker-compose build
docker-compose up

A API ficará acessível em http://localhost:5000
🧶 Opção B: ambiente virtual Python

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app.py
export MONGO_URI="mongodb://localhost:27017/minha_db"
export FLASK_ENV=development

flask run

🧪 Testes & Lint

Execute:

make test      # flake8 + pytest
# ou
make flake     # apenas lint

🧩 Pipeline CI com GitHub Actions

O workflow Deploy Render realiza:

    Lint com flake8

    Testes com pytest

    (Opcional) Deploy automático no Render via hook, se estiver configurado

O arquivo está em .github/workflows/render-deploy.yml.
🌐 Deploy em Render

Se o auto-deploy estiver ativado, Render fará o build e deploy após push no main.

Caso queira controlar via GitHub Actions, configure:

    Deploy Hook no dashboard do Render

    Adicione RENDER_DEPLOY_HOOK como secret

    Inclua o passo no final da pipeline:

- name: Trigger Render Deploy
  if: success()
  run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}

📁 Estrutura de pastas

.
├── app.py               # ponto de entrada Flask
├── requirements.txt     # dependências pip
├── Makefile             # tarefas úteis (test, compose, lint)
├── docker-compose.yml   # ambiente com Flask + MongoDB
├── .github/             # workflows do GitHub Actions
└── tests/               # testes unitários pytest

⭐ Melhorias futuras

    Adicionar autenticação JWT

    Usar Flask-RESTful ou FastAPI

    Implementar validação com marshmallow ou pydantic

    Adicionar endpoint de health check

    Habilitar ambientes staging e production

    Adicionar documentação Swagger/OpenAPI

✅ Licença

Este projeto está sob a licença MIT — sinta-se à vontade para usar, editar e distribuir!
🤝 Autor

Igor Rodrigues — github.com/igorrodriguesss

Entre em contato se quiser bater um papo sobre melhorias ou colaborações! 😊


---

Se quiser que eu atualize com um print da API em execução, link do Render ou mais seções (e
