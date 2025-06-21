import streamlit as st
import pandas as pd
import os

dat = pd.read_csv(file_path, index_col=0)
# Sidebar inputs
drug = st.text_input("Enter drug name: (e.g. pazopanib...)")
cell_line = st.selectbox("Select Cell Line", ['A549','MCF7','PC3', 'VCAP', 'MDAMB231', 'BT20', 'HT29', 'A375', 'HELA'])
type = st.selectbox("Select data type", ['chemical','genetic'])

if st.button("Load DEGs"):
    file_path = f"data/{type}_top20degs_{cell_line}.csv"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        dat = pd.read_csv(f'data/{type}_top20degs_{cell_line}.csv', index_col=0)
        dat = df[df["condition"] == drug]
        st.write(f"Showing top 10 DEGs for cell line {cell_line} with {type} perturbagen: {drug}")
        st.dataframe(dat)

