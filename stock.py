import streamlit as st
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("Google Sheets as a Database")

# Accessing Google Sheets credentials from Streamlit Secrets
credentials_dict = st.secrets["gsheets"]

# Authenticate with Google
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# Open Google Sheets
spreadsheet_url = "https://docs.google.com/spreadsheets/d/18PgkCySwFnghk_iHsW6bpzkqjnbtsbG4y-UH_dinO_E/edit#gid=0"
sheet = client.open_by_url(spreadsheet_url).sheet1

# Read data from Google Sheets
df = get_as_dataframe(sheet)
st.write("Data from Google Sheets:")
st.write(df)

# Write data to Google Sheets
if st.button("Write to Google Sheets"):
    new_data = pd.DataFrame({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})
    set_with_dataframe(sheet, new_data)
    st.success("Data written to Google Sheets successfully!")
