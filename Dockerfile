# Usar uma imagem base com Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de requisitos
COPY requirements.txt /app/

# Atualizar pacotes do sistema e instalar venv
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Adicionar o ambiente virtual ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copiar o código do projeto
COPY . /app/

# Expor a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
