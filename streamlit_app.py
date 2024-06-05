import streamlit as st
import pandas as pd
import numpy as np

st.title('四字熟語ガチャ')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

a = np.random.choice(words_df)
b = words_df[words_df['単語'] == a]

if st.button('四字熟語を見る'):
    print(b)
