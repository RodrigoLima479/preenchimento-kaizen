import streamlit as st
import pandas as pd
import time
from playwright.sync_api import sync_playwright

st.set_page_config(page_title="ValeForms Web", layout="wide")

st.title("ValeForms Web")

# Upload de arquivos
uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Leitura do arquivo
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("Dados carregados:")
    st.dataframe(df)

    # Aqui você pode colocar a integração com Playwright
    if st.button("Processar Formulário"):
        with st.spinner("Executando Playwright..."):
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                # Coloque aqui o código do Playwright para preencher os formulários
                time.sleep(2)
                browser.close()
            st.success("Formulário processado com sucesso!")
