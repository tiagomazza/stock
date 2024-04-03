import streamlit as st
import pandas as pd
import json

st.title("Google Sheets as a Database")

# Function to create a sample Orders dataframe
def create_orders_dataframe():
    return pd.DataFrame({
        'OrderID': [101, 102, 103, 104, 105],
        'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'ProductList': ['ProductA, ProductB', 'ProductC', 'ProductA, ProductC', 'ProductB, ProductD', 'ProductD'],
        'TotalPrice': [200, 150, 250, 300, 100],
        'OrderDate': ['2023-08-18', '2023-08-19', '2023-08-19', '2023-08-20', '2023-08-20']
    })

# Create the Orders dataframe
orders = create_orders_dataframe()

# Update the TotalPrice column in the orders dataframe to create updated_orders
updated_orders = orders.copy()
updated_orders['TotalPrice'] = updated_orders['TotalPrice'] * 100

with st.expander("Data ⤵"):
    st.write("Orders")
    st.dataframe(orders)
    st.write("Updated Orders")
    st.dataframe(updated_orders)

st.divider()
st.write("CRUD Operations:")

# Reading credentials from Streamlit secrets
try:
    credentials_dict = json.loads(st.secrets["gsheets"])
except KeyError:
    st.error("Google Sheets credentials not found in Streamlit secrets. Please set up the credentials.")
    st.stop()

# You can access each credential like this:
# service_account_email = credentials_dict["client_email"]
# private_key = credentials_dict["private_key"]

# You can also directly pass the credentials dictionary to the connection
# Establishing a Google Sheets connection
conn = st.experimental_gsheets(credentials_dict)

# Taking actions based on user input
if st.button("New Worksheet"):
    conn.create(worksheet="Orders", data=orders)
    st.success("Worksheet Created 🎉")

if st.button("Calculate Total Orders Sum"):
    sql = 'SELECT SUM("TotalPrice") as "TotalOrdersPrice" FROM Orders;'
    total_orders = conn.query(sql=sql)  # default ttl=3600 seconds / 60 min
    st.dataframe(total_orders)

if st.button("Update Worksheet"):
    conn.update(worksheet="Orders", data=updated_orders)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="Orders")
    st.success("Worksheet Cleared 🧹")
