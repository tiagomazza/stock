import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurações da aplicação Streamlit
st.title("Escrever no Google Sheets")
st.write("Esta aplicação escreve dados em uma planilha do Google Sheets.")

# Autenticação e acesso ao Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Abrir a planilha do Google Sheets
spreadsheet_url = "https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit#gid=0"
sheet = client.open_by_url(spreadsheet_url).sheet1

# Função para escrever dados na planilha
def escrever_dados(dados):
    sheet.append_row(dados)
    st.success("Dados adicionados com sucesso!")

# Interface do Streamlit para escrever dados
dados_input = st.text_input("Digite os dados separados por vírgula:")
if st.button("Adicionar Dados"):
    dados = dados_input.split(",")
    escrever_dados(dados)
