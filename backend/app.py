from flask import Flask, jsonify
import random
import json
import os

# Caminho relativo ao diretório deste arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'products.json')

# Carrega a lista de produtos ao iniciar a aplicação
with open(DATA_PATH, encoding='utf-8') as f:
    products = json.load(f)

app = Flask(__name__)


@app.route('/api/products', methods=['GET'])
def get_products():
    """Retorna a lista de produtos disponíveis."""
    return jsonify(products)


@app.route('/api/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id: str):
    """
    Gera recomendações para um usuário.
    A implementação atual seleciona aleatoriamente alguns produtos
    como recomendação de demonstração.
    """
    # define quantas recomendações devolver
    quantity = 3
    # se houver menos produtos do que o desejado, ajusta
    n = min(quantity, len(products))
    recommended = random.sample(products, n)
    return jsonify({
        'user_id': user_id,
        'recommendations': recommended
    })


if __name__ == '__main__':
    # Roda a aplicação em modo debug para facilitar testes locais
    app.run(host='0.0.0.0', port=5000, debug=True)
