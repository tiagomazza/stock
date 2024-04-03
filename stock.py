import streamlit as st
from streamlit_gsheets import GSheetClient

st.title("Read Google Sheet as DataFrame")

client = st.experimental_gcs_client()

with client.open_by_url("https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit#gid=0") as sh:
    worksheet = sh.worksheet("Pag1")
    df = worksheet.get_as_df()

st.dataframe(df)
