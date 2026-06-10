# ── Estágio de build ─────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ── Imagem final ──────────────────────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Copiar dependências instaladas do estágio de build
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copiar código da aplicação
COPY app.py .

# Porta que o App Runner espera
EXPOSE 8080

# Usuário não-root por segurança
RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]
