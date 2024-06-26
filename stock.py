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

if product_id:
    # Recupera o estoque atual
    if variation_id:
        endpoint = f"products/{product_id}/variations/{variation_id}"
    else:
        endpoint = f"products/{product_id}"
    
    response = wcapi.get(endpoint).json()
    
    if "stock_quantity" in response:
        current_stock = response["stock_quantity"]
        st.write(f"Estoque atual: {current_stock}")
    else:
        st.error(f"Erro ao obter estoque atual: {response.get('message', 'Erro desconhecido')}")
        current_stock = None
else:
    current_stock = None

new_stock = st.number_input("Novo Estoque", min_value=0, step=1)

if st.button("Atualizar Estoque"):
    if product_id and new_stock is not None and current_stock is not None:
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
            st.success(f"Estoque do produto {'variação ' + variation_id if variation_id else product_id} atualizado de {current_stock} para {new_stock}.")
        else:
            st.error(f"Erro ao atualizar estoque: {response.get('message', 'Erro desconhecido')}")
    else:
        st.warning("Por favor, insira um ID de produto válido e quantidade de estoque.")
