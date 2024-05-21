import streamlit as st
from woocommerce import API

# Configuração da API do WooCommerce
wcapi = API(
    url="https://shop.quintaclandestina.pt",  # Substitua pelo URL da sua loja
    consumer_key="ck_326fe2832e12ff0ee0f2dd4a32e87ee0ceada496",   # Substitua pela sua Consumer Key
    consumer_secret="cs_44ad7b5fc9a38d6212240cbded4119636d003545",
    version="wc/v3"
)

st.title("Gerenciamento de Estoque WooCommerce")

# Formulário para entrada de dados
product_id = st.text_input("ID do Produto")
variation_id = st.text_input("ID da Variação (deixe em branco se não for uma variação)")
new_stock = st.number_input("Novo Estoque", min_value=0, step=1)

if st.button("Atualizar Estoque"):
    if product_id and new_stock is not None:
        if variation_id:
            # Atualiza o estoque de uma variação de produto no WooCommerce
            endpoint = f"
