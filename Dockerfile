# ========================
# Stage 1 — Build
# ========================
FROM python:3.11-slim AS builder

WORKDIR /build

# Dependências de sistema (apenas para build)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas dependências para aproveitar cache
COPY requirements.txt .

# Instala dependências em diretório isolado
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt


# ========================
# Stage 2 — Runtime
# ========================
FROM python:3.11-slim

WORKDIR /app

# Copia somente o que foi instalado no stage de build
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY . .

# Variáveis padrão para Flask
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Porta padrão Flask (ajuste se necessário)
EXPOSE 5000

# Comando de inicialização
CMD ["python", "run.py"]
