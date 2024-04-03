import streamlit as st
import gspread
from google.oauth2 import service_account

# Obter as credenciais do Streamlit Secrets
credentials_json = st.secrets["gcp_service_account"]

# Autenticar com o Google Sheets usando as credenciais
credentials = service_account.Credentials.from_service_account_info(credentials_json)
gc = gspread.authorize(credentials)

# Abrir a planilha
spreadsheet_url = "https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit?usp=drive_link"
sh = gc.open_by_url(spreadsheet_url)

# Ler os dados da planilha
worksheet = sh.sheet1
data = worksheet.get_all_values()

# Mostrar os dados lidos da planilha
st.write("Dados da planilha:")
st.write(data)

# Escrever dados na planilha
if st.button("Escrever na planilha"):
    new_data = [
        ["Novo Dado 1", "Novo Dado 2", "Novo Dado 3"],
        ["Outro Novo Dado 1", "Outro Novo Dado 2", "Outro Novo Dado 3"]
    ]
    worksheet.append_rows(new_data)
    st.success("Dados adicionados com sucesso!")

# Atualizar os dados lidos da planilha
data = worksheet.get_all_values()

# Mostrar os dados atualizados da planilha
st.write("Dados atualizados da planilha:")
st.write(data)
