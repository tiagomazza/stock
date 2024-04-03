import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurações da aplicação Streamlit
st.title("Acesso ao Google Sheets")
st.write("Esta aplicação acessa um Google Sheets público.")

# Autenticação e acesso ao Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Abre o Google Sheets
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit#gid=0").sheet1

# Função para escrever dados
def escrever_dados(dados):
    sheet.append_row(dados)
    st.success("Dados adicionados com sucesso!")

# Função para apagar dados
def apagar_dados():
    sheet.clear()
    st.success("Todos os dados foram apagados!")

# Interface do Streamlit
opcao = st.radio("Escolha uma opção:", ("Escrever Dados", "Apagar Dados"))

if opcao == "Escrever Dados":
    dados = st.text_input("Digite os dados separados por vírgula:")
    if st.button("Adicionar Dados"):
        dados = dados.split(",")
        escrever_dados(dados)
elif opcao == "Apagar Dados":
    if st.button("Apagar Todos os Dados"):
        apagar_dados()
