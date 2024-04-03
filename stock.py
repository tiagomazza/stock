import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import toml

# Título da aplicação
st.title("Google Sheets as a Database")

# Função para criar um dataframe de exemplo
def create_orders_dataframe():
    return pd.DataFrame({
        'OrderID': [101, 102, 103, 104, 105],
        'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'ProductList': ['ProductA, ProductB', 'ProductC', 'ProductA, ProductC', 'ProductB, ProductD', 'ProductD'],
        'TotalPrice': [200, 150, 250, 300, 100],
        'OrderDate': ['2023-08-18', '2023-08-19', '2023-08-19', '2023-08-20', '2023-08-20']
    })

# Carregar as credenciais do arquivo TOML
credentials_toml_string = st.secrets["gsheets"]
credentials_toml = toml.loads(credentials_toml_string)

# Criar o dataframe de pedidos
orders = create_orders_dataframe()

# Atualizar a coluna TotalPrice no dataframe de pedidos para criar updated_orders
updated_orders = orders.copy()
updated_orders['TotalPrice'] = updated_orders['TotalPrice'] * 100

# Mostrar os dataframes na interface do Streamlit
with st.expander("Data ⤵"):
    st.write("Orders")
    st.dataframe(orders)
    st.write("Updated Orders")
    st.dataframe(updated_orders)

# Estabelecer uma conexão com o Google Sheets usando as credenciais
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_toml, scope)
client = gspread.authorize(creds)

# Abrir a planilha do Google Sheets
spreadsheet_url = credentials_toml["connections.gsheets"]["spreadsheet"]
worksheet = client.open_by_url(spreadsheet_url).sheet1

# Operações CRUD com base na entrada do usuário
if st.button("New Worksheet"):
    worksheet.clear()
    worksheet.append_rows(orders.values.tolist())
    st.success("Worksheet Created 🎉")

if st.button("Calculate Total Orders Sum"):
    total_orders_price = worksheet.acell('G1').value
    st.write(f"Total Orders Price: {total_orders_price}")

if st.button("Update Worksheet"):
    worksheet.clear()
    worksheet.append_rows(updated_orders.values.tolist())
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    worksheet.clear()
    st.success("Worksheet Cleared 🧹")
