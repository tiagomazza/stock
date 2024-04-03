import streamlit as st
import gspread
from streamlit.credentials import get_credentials

# Obtém as credenciais do Streamlit Secrets
credentials = get_credentials()["gcp"]["access_token"]

# Autentica com o Google Sheets
gc = gspread.authorize(credentials)

# Abre a planilha
spreadsheet_url = "https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit?usp=drive_link"
sh = gc.open_by_url(spreadsheet_url)

# Lê os dados da planilha
worksheet = sh.sheet1
data = worksheet.get_all_values()

# Mostra os dados lidos da planilha
st.write("Dados da planilha:")
st.write(data)

# Escreve dados na planilha
if st.button("Escrever na planilha"):
    new_data = [
        ["Novo Dado 1", "Novo Dado 2", "Novo Dado 3"],
        ["Outro Novo Dado 1", "Outro Novo Dado 2", "Outro Novo Dado 3"]
    ]
    worksheet.append_rows(new_data)
    st.success("Dados adicionados com sucesso!")

# Atualiza os dados lidos da planilha
data = worksheet.get_all_values()

# Mostra os dados atualizados da planilha
st.write("Dados atualizados da planilha:")
st.write(data)
