import streamlit as st
import pandas as pd

# Sidebar inputs
drug = st.text_input("Enter drug name:")
cell_line = st.selectbox("Select Cell Line", ['A549','MCF7','PC3', 'VCAP', 'MDAMB231', 'BT20', 'HT29', 'A375', 'HELA'])
type = st.selectbox("Select data type", ['chemical','genetic'])

dat = pd.read_csv(f'data/{type}_top20degs_{cell_line}.csv', index_col=0)

# Filter results
dat = df[df["condition"] == drug]

# Show DEGs
st.write(f"Showing top 10 DEGs for cell line {cell_line} with {type} perturbagen: {drug}")
st.dataframe(dat[['names','logfoldchanges']])
