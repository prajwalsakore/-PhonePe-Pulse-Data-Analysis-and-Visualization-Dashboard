#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Connect to the MySQL database
def get_data_from_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@1234",
        database="phonepe_data"
    )
    query = "SELECT * FROM transactions;"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Load data
df = get_data_from_db()

# Sidebar for filters
st.sidebar.title("Filters")
states = df['state'].unique()
selected_state = st.sidebar.selectbox("Select State", states)

years = df['year'].unique()
selected_year = st.sidebar.selectbox("Select Year", years)

transaction_types = df['type'].unique()
selected_type = st.sidebar.selectbox("Select Transaction Type", transaction_types)

# Filtered data
filtered_df = df[(df['state'] == selected_state) & 
                 (df['year'] == selected_year) & 
                 (df['type'] == selected_type)]

# Displaying Data
st.title(f"PhonePe Transactions Analysis - {selected_state} ({selected_year})")
st.write(f"Transaction Type: {selected_type}")

# Plotting a Bar Chart
fig = px.bar(filtered_df, x='quarter', y='amount', color='name', title="Transaction Amount by Quarter")
st.plotly_chart(fig)

# Plotting a Pie Chart
fig = px.pie(filtered_df, names='name', values='amount', title="Distribution of Transaction Amount by Category")
st.plotly_chart(fig)


# In[ ]:




