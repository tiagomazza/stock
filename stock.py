import streamlit as st
from woocommerce import API

# Configuração da API do WooCommerce
wcapi = API(
    url="https://shop.quintaclandestina.pt",  # Substitua pelo URL da sua loja
    consumer_key="ck_326fe2832e12ff0ee0f2dd4a32e87ee0ceada496",   # Substitua pela sua Consumer Key
    consumer_secret="cs_44ad7b5fc9a38d6212240cbded4119636d003545",
    version="wc/v3"
)

if st.button("Atualizar Estoque"):
    if product_id and new_stock is not None:
        if variation_id:
            # Atualiza o estoque de uma variação de produto no WooCommerce
            endpoint = f"products/{product_id}/variations/{variation_id}"
        else:
            # Atualiza o estoque de um produto simples no WooCommerce
            endpoint = f"products/{product_id}"
        
        # Dados para atualização do estoque
        data = {
            "stock_quantity": new_stock
        }
        
        # Envia a solicitação para atualizar o produto ou variação
        response = wcapi.put(endpoint, data).json()
        
        if "id" in response:
            st.success(f"Estoque do produto {'variação ' + variation_id if variation_id else product_id} atualizado para {new_stock}.")
        else:
            st.error(f"Erro ao atualizar estoque: {response.get('message', 'Erro desconhecido')}")
    else:
        st.warning("Por favor, insira um ID de produto válido e quantidade de estoque.")
