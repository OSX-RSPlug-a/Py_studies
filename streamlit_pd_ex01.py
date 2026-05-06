import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Random data explorer", Layout="centered")

st.title("Random data emplerer")


st.sidebar.header("Settings")

pointer = st.sidebar.slider("Number of data points", 10, 500, 100)

seed = st.sidebar.number_input("Random seed", value=42)

generate = st.sidebar.button("Generate data")


if generate:
    np.random.seed(seed)
    
    data = {
        "x": np.linspace(0, 10, points),
        "y": np.sin(np.linspace(0, 10, points)) + np.random.normal(0, 0.5, points)
    }
    
    df. pd.DataFrame(data)
    
    st.success("Data genareted")
    
    st.line_chart(df)
    
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.info("Use the sidebar to generate data")