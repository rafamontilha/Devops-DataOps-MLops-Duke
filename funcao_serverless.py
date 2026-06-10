"""Função Serverless - Invoca o microsserviço no App Runner
Módulo 1 - Questão 3: Função sem servidor

Compatível com:
  - AWS Lambda (handler = lambda_handler)
  - Google Cloud Functions (handler = gcf_handler)
  - Execução local para teste

Variável de ambiente necessária:
  APP_RUNNER_URL = https://<seu-id>.us-east-1.awsapprunner.com
"""

import json
import os
import urllib.request
import urllib.error


# URL do serviço no App Runner (configurar como variável de ambiente)
APP_RUNNER_URL = os.getenv("APP_RUNNER_URL", "http://localhost:8080")


def obter_fruta_aleatoria(url_base: str) -> dict:
    """Chama o endpoint /fruta do microsserviço e retorna o resultado."""
    url = f"{url_base}/fruta"
    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            corpo = resposta.read().decode("utf-8")
            return {"sucesso": True, "dados": json.loads(corpo)}
    except urllib.error.HTTPError as erro:
        return {"sucesso": False, "erro": f"HTTP {erro.code}: {erro.reason}"}
    except urllib.error.URLError as erro:
        return {"sucesso": False, "erro": str(erro.reason)}


# ── AWS Lambda ────────────────────────────────────────────────────────────────
def lambda_handler(event, context):  # pylint: disable=unused-argument
    """Ponto de entrada para AWS Lambda."""
    resultado = obter_fruta_aleatoria(APP_RUNNER_URL)

    status = 200 if resultado["sucesso"] else 502
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(resultado),
    }


# ── Google Cloud Functions ────────────────────────────────────────────────────
def gcf_handler(request):  # pylint: disable=unused-argument
    """Ponto de entrada para Google Cloud Functions."""
    resultado = obter_fruta_aleatoria(APP_RUNNER_URL)
    status = 200 if resultado["sucesso"] else 502
    return json.dumps(resultado), status, {"Content-Type": "application/json"}


# ── Execução local ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Invocando serviço em: {APP_RUNNER_URL}")
    res = obter_fruta_aleatoria(APP_RUNNER_URL)
    print(json.dumps(res, indent=2, ensure_ascii=False))
