import streamlit as st
import pandas as pd

# Sidebar inputs
drug = st.text_input("Enter drug name: (e.g. pazopanib...)")
cell_line = st.selectbox("Select Cell Line", ['A549','MCF7','PC3', 'VCAP', 'MDAMB231', 'BT20', 'HT29', 'A375', 'HELA'])
type = st.selectbox("Select data type", ['chemical','genetic'])

if st.button("Load DEGs"):
    dat = pd.read_csv(f'data/{type}_top20degs_{cell_line}.csv', index_col=0)
    dat = df[df["condition"] == drug]
    st.write(f"Showing top 10 DEGs for cell line {cell_line} with {type} perturbagen: {drug}")
    st.dataframe(dat)

