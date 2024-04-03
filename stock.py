import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)



for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
    except Exception as e:
    st.error(f"Erro ao ler dados do Google Sheets: {e}")

