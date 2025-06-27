# 🐍 REST API com Flask & MongoDB

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/igorrodriguesss/restapi-flask/render-deploy.yml?branch=main)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Este projeto é uma API REST construída com **Flask**, persistindo dados em **MongoDB**, e preparada para deploy utilizando **Docker** e **Render**. Conta também com testes, linting e pipeline CI/CD com **GitHub Actions**.

## 🔧 Tecnologias

- Linguagem: **Python 3.9+**
- Framework web: **Flask**
- Banco de dados: **MongoDB**
- Testes: **pytest**
- Linting: **flake8**
- CI/CD: **GitHub Actions**
- Containerização: **Docker & Docker Compose**
- Deploy remoto: **Render** (via Webhook manual)

## 🚀 Como rodar localmente

### Pré-requisitos

- Docker
- Docker Compose

### Passos

```bash
docker-compose build
docker-compose up
# A API ficará acessível em: http://localhost:5000
```

## 🧪 Testes & Lint

```bash
make test      # flake8 + pytest
# ou
make flake     # apenas lint
```

## 🧩 Pipeline CI com GitHub Actions

O workflow `Deploy Render` realiza:

1. Lint com flake8  
2. Testes com pytest  
3. Deploy manual para o Render via **Deploy Hook**

O arquivo está localizado em:

```text
.github/workflows/render-deploy.yml
```

## 🌐 Deploy no Render

O deploy **não é automático**. Ele só ocorre quando a pipeline do GitHub Actions é executada com sucesso.

### Como configurar:

1. Gere um **Deploy Hook** no painel da Render (Settings > Deploy Hooks)  
2. Adicione o link como secret no GitHub:
   - Nome: `RENDER_DEPLOY_HOOK`
3. No final do workflow, o deploy é acionado com:

```yaml
- name: Trigger Render Deploy
  if: success()
  run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

## 🗂️ Estrutura de pastas

```text
.
├── app.py               # ponto de entrada Flask
├── requirements.txt     # dependências pip
├── Makefile             # tarefas úteis (test, compose, lint)
├── docker-compose.yml   # ambiente com Flask + MongoDB
├── .github/             # workflows do GitHub Actions
└── tests/               # testes unitários pytest
```

## 🧱 Diagrama da arquitetura

> ![Arquitetura do projeto](docs/arquitetura.png)

💡 Para adicionar ao seu projeto:
1. Crie uma pasta `docs/`
2. Salve a imagem do diagrama com o nome `arquitetura.png` dentro dela
3. Faça commit/push para aparecer no GitHub

## ⭐ Melhorias futuras

- Adicionar autenticação JWT  
- Usar Flask-RESTful ou FastAPI  
- Implementar validação com `marshmallow` ou `pydantic`  
- Adicionar endpoint de health check  
- Separar ambientes de staging e produção  
- Adicionar documentação Swagger/OpenAPI  

## ✅ Licença

Este projeto está sob a licença **MIT** — sinta-se à vontade para usar, editar e distribuir!

