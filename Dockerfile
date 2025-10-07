# Imagem base
FROM python:3.13-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    wget curl gnupg unzip libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libpango-1.0-0 libpangocairo-1.0-0 \
    libasound2 fonts-liberation libwoff1 libxshmfence1 xdg-utils libgtk-3-0 libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Instala Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Instala Playwright browsers
RUN playwright install

# Expondo porta do Streamlit
EXPOSE 8501

# Comando para rodar app Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
