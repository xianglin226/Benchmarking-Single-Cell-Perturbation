import streamlit as st
import pandas as pd
import os

drug = st.text_input("Enter drug name: (e.g. pazopanib...)")
cell_line = st.selectbox("Select Cell Line", ['A549','MCF7','PC3', 'VCAP', 'MDAMB231', 'BT20', 'HT29', 'A375', 'HELA'])
type = st.selectbox("Select data type", ['chemical','genetic'])

if st.button("Load DEGs"):
    file_path = f"/mount/src/benchmarking-single-cell-perturbation/FastPert/data/{type}_top20degs_{cell_line}.csv"
    if not os.path.exists(file_path):
        st.write(f"DEGs not found for: {cell_line} with {drug}")
    else:
        dat = pd.read_csv(file_path, index_col=0)
        dat = dat[dat["condition"] == drug]
        dat = dat.sort_values(by="logfoldchanges", ascending=False)
        dat = dat[['names','logfoldchanges']]
        dat = dat.reset_index(drop=True)
        st.write(f"Showing top 20 DEGs for cell line {cell_line} with {type} perturbagen: {drug}")
        st.dataframe(dat)

