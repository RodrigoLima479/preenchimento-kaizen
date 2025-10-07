# app.py
import streamlit as st
import pandas as pd
import time
from pathlib import Path
import subprocess
import sys

# --- Instala os navegadores do Playwright ---
#subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

# --- Agora sim podemos importar o Playwright ---
from playwright.sync_api import sync_playwright

st.set_page_config(page_title="ValeFormsWeb", layout="wide")
st.title("💻 ValeForms Web - Automatização de Formulários")

# --- Upload de CSV ---
uploaded_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

if uploaded_file:
    # Lê CSV
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Erro ao ler o CSV: {e}")

    # Botão para iniciar o preenchimento
    if st.button("Iniciar preenchimento"):
        with st.spinner("Executando preenchimento..."):
            total = len(df)
            progresso_bar = st.progress(0)

            # Inicializa Playwright
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)  # Headless=True se quiser rodar sem abrir navegador
                page = browser.new_page()

                for i, row in df.iterrows():
                    # --- Aqui você coloca o seu código de preenchimento ---
                    # Exemplo genérico:
                    matricula = row.get("Matricula", "")
                    nome = row.get("Nome", "")
                    st.write(f"Preenchendo: {matricula} - {nome}")
                    
                    # Simula tempo de preenchimento
                    time.sleep(1)

                    # Atualiza barra de progresso
                    progresso_bar.progress(int(((i + 1) / total) * 100))

                browser.close()

            st.success("Preenchimento concluído!")
