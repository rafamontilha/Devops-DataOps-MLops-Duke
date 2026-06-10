"""Microsserviço Flask - Frutas Aleatórias
Módulo 1 - Curso DevOps/DataOps/MLOps
"""

import random
from flask import Flask, jsonify

app = Flask(__name__)

FRUTAS = [
    "Maçã", "Banana", "Manga", "Abacaxi", "Uva",
    "Morango", "Melancia", "Laranja", "Pêssego", "Kiwi",
    "Goiaba", "Caju", "Maracujá", "Pitaya", "Acerola",
]


@app.route("/")
def home():
    """Endpoint raiz com instruções de uso."""
    return jsonify({
        "servico": "Frutas Aleatórias",
        "versao": "1.0.0",
        "endpoints": {
            "/fruta": "Retorna uma fruta aleatória",
            "/frutas": "Retorna todas as frutas disponíveis",
            "/saude": "Verifica saúde do serviço",
        },
    })


@app.route("/fruta")
def fruta_aleatoria():
    """Retorna uma fruta escolhida aleatoriamente."""
    fruta = random.choice(FRUTAS)
    return jsonify({"fruta": fruta})


@app.route("/frutas")
def listar_frutas():
    """Retorna a lista completa de frutas."""
    return jsonify({"total": len(FRUTAS), "frutas": FRUTAS})


@app.route("/saude")
def saude():
    """Health check para o App Runner / load balancer."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
