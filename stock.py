import streamlit as st
from streamlit_gsheets import GSheetsConnection

try:
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Lê os dados da planilha
    df = conn.read(
        worksheet="Página1",
        ttl="10m",
        usecols=[0, 1],
        nrows=3,
    )

    # Mostra os resultados
    for row in df.itertuples():
        st.write(f"{row.name} has a {row.pet}")
except Exception as e:
    st.error(f"Erro ao ler dados do Google Sheets: {e}")


