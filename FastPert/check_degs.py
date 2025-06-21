import streamlit as st
import pandas as pd

# Sidebar inputs
drug = st.text_input("Enter drug name:")
cell_line = st.selectbox("Select Cell Line", df["cell_line"].unique())
type = st.selectbox("Select data type", ['chemical','genetic'])

dat = pd.read_csv(f'data/{type}_top20degs_{cell_line}.csv', index_col=0)

# Filter results
dat = df[df["condition"] == drug]

# Show DEGs
st.write(f"Showing top 10 DEGs for cell line {cell_line} with {type} perturbagen: {drug}")
st.dataframe(dat[['names','logfoldchanges']])
