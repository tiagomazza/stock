import streamlit as st
from woocommerce import API

# Configuração da API do WooCommerce
wcapi = API(
    url="https://sua-loja.com",  # Substitua pelo URL da sua loja
    consumer_key="ck_xxxxxxx",   # Substitua pela sua Consumer Key
    consumer_secret="cs_xxxxxxx",  # Substitua pelo seu Consumer Secret
    version="wc/v3"
)

st.title("Gerenciamento de Estoque WooCommerce")

# Formulário para entrada de dados
product_id = st.text_input("ID do Produto")
new_stock = st.number_input("Novo Estoque", min_value=0, step=1)

if st.button("Atualizar Estoque"):
    if product_id and new_stock is not None:
        # Atualiza o estoque do produto no WooCommerce
        data = {
            "stock_quantity": new_stock
        }
        response = wcapi.put(f"products/{product_id}", data).json()
        
        if "id" in response:
            st.success(f"Estoque do produto {product_id} atualizado para {new_stock}.")
        else:
            st.error(f"Erro ao atualizar estoque: {response.get('message', 'Erro desconhecido')}")
    else:
        st.warning("Por favor, insira um ID de produto válido e quantidade de estoque.")

