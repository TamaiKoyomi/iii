import streamlit as st
import pandas as pd
import numpy as np

st.title('四字熟語ガチャ')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

if st.button('四字熟語を見る'):
    rarity_probs = {
        'N': 0.4,
        'R': 0.3,
        'SR': 0.2,
        'SSR': 0.1
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))
    subset_df = words_df[words_df['レア度'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"単語名: {st.session_state.selected_word['単語']}")
    st.subheader(f"レア度: {st.session_state.selected_word['レア度']}")

    # 意味を確認するボタンを追加
    if st.button('意味を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"意味: {st.session_state.selected_word['意味']}")