"""Testes do microsserviço Flask - Frutas Aleatórias
Módulo 1 - CI personalizado
"""

import pytest
from app import app, FRUTAS


@pytest.fixture
def client():
    """Cria cliente de teste Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Testes do endpoint raiz ──────────────────────────────────────────────────

def test_home_retorna_200(client):
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_home_contem_chave_servico(client):
    dados = client.get("/").get_json()
    assert "servico" in dados


def test_home_contem_endpoints(client):
    dados = client.get("/").get_json()
    assert "endpoints" in dados


# ── Testes do endpoint /fruta ────────────────────────────────────────────────

def test_fruta_retorna_200(client):
    resposta = client.get("/fruta")
    assert resposta.status_code == 200


def test_fruta_retorna_json_com_chave(client):
    dados = client.get("/fruta").get_json()
    assert "fruta" in dados


def test_fruta_esta_na_lista(client):
    dados = client.get("/fruta").get_json()
    assert dados["fruta"] in FRUTAS


def test_fruta_multiplas_chamadas_sao_validas(client):
    """Garante que múltiplas chamadas sempre retornam frutas válidas."""
    for _ in range(20):
        dados = client.get("/fruta").get_json()
        assert dados["fruta"] in FRUTAS


# ── Testes do endpoint /frutas ───────────────────────────────────────────────

def test_frutas_retorna_200(client):
    resposta = client.get("/frutas")
    assert resposta.status_code == 200


def test_frutas_contem_lista(client):
    dados = client.get("/frutas").get_json()
    assert "frutas" in dados
    assert isinstance(dados["frutas"], list)


def test_frutas_total_correto(client):
    dados = client.get("/frutas").get_json()
    assert dados["total"] == len(FRUTAS)


# ── Testes do health check ───────────────────────────────────────────────────

def test_saude_retorna_200(client):
    resposta = client.get("/saude")
    assert resposta.status_code == 200


def test_saude_retorna_status_ok(client):
    dados = client.get("/saude").get_json()
    assert dados["status"] == "ok"
