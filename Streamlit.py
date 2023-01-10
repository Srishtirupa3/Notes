import streamlit as st
import pandas as pd
import numpy as np

st.text("Welcome to Streamlit")


df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(df)

st.bar_chart(df)