# Projeto 1 – Aplicação de recomendação com IA

Este repositório contém um protótipo de uma aplicação web de recomendação de produtos.  
Ele foi concebido para servir como um projeto de portfólio e demonstra integração entre
um back‑end em Python, um front‑end simples em HTML/JavaScript e um modelo
de recomendação baseado em dados. Embora a versão atual utilize recomendações
aleatórias como prova de conceito, a estrutura foi preparada para que você possa
substituir essa lógica por um algoritmo de machine learning real.

## Estrutura

- `backend/` – API REST escrita em Flask. Ela disponibiliza dois endpoints principais:
  - `GET /api/products`: retorna a lista de produtos do arquivo JSON de dados.
  - `GET /api/recommendations/<user_id>`: devolve algumas recomendações para
    o usuário informado. No momento, a implementação devolve produtos aleatórios
    de `data/products.json` para simplificar.
- `data/products.json` – Base de dados de exemplo com produtos. Você pode
  expandi‑la ou substituí‑la por outra fonte de dados.
- `frontend/index.html` – Página web simples que consome a API usando
  JavaScript vanilla. Ela exibe os produtos disponíveis e as recomendações
  geradas para um usuário fictício.

## Como executar

### Pré‑requisitos

Certifique‑se de ter o Python 3 instalado em sua máquina. Recomenda‑se o
uso de um ambiente virtual para isolar as dependências.

### Passo a passo

1. Instale as dependências do back‑end:

```
bash
cd project1/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Inicie a API:

```
bash
python app.py
```

3. Abra o arquivo `frontend/index.html` em seu navegador. A página irá
solicitar os dados da API rodando na porta 5000 e exibirá a lista de produtos
e as recomendações geradas.

## Próximos passos

- **Recomendação inteligente:** substitua a função de recomendação aleatória
  por um modelo de machine learning. Você pode implementar filtragem
  colaborativa ou um sistema baseado em conteúdo com bibliotecas como
  Scikit‑Learn ou TensorFlow.
- **Interface moderna:** substitua a página HTML por um front‑end moderno
  utilizando React, Next.js ou outra biblioteca que preferir.
- **Testes e CI/CD:** adicione testes automatizados (por exemplo com
  PyTest) e configure um pipeline de integração contínua (GitHub Actions) para
  validar e implantar a aplicação automaticamente.
