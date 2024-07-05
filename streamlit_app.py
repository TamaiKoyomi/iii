import streamlit as st
import pandas as pd
import numpy as np

st.title('四字熟語ガチャ')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

def judge(kategori):
    if st.button(kategori) and st.session_state.selected_word['分類']==kategori:
            return True
    else:
        return False

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
    st.subheader(f"読み方：{st.session_state.selected_word['読み方']}")
    st.subheader(f"レア度: {st.session_state.selected_word['レア度']}")

    st.write('この四字熟語は、次の選択肢のうちどれに分類されるでしょう？(Chat GPTが分類しました。違うと思っても怒らないでください。)')

    kategori=['文学・哲学的なテーマ性','行動・精神的な特性','自然・現象に関連するもの']

    for bunrui in kategori:
        if judge==True:
            st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
            if st.button('意味を確認する'):
                st.session_state.display_meaning = True

            if st.session_state.display_meaning:
                st.write(f"意味: {st.session_state.selected_word['意味']}")

        elif judge==False:
            st.write('残念、違います。正しい意味を確認して、この四字熟語をマスターしましょう！')
            if st.button('意味を確認する'):
                st.session_state.display_meaning = True

            if st.session_state.display_meaning:
                st.write(f"意味: {st.session_state.selected_word['意味']}")




'''    if st.button('文学・哲学的なテーマ性') and st.session_state.selected_word['分類']=='文学・哲学的なテーマ性'
        st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
        if st.button('意味を確認する'):
            st.session_state.display_meaning = True

        if st.session_state.display_meaning:
            st.write(f"意味: {st.session_state.selected_word['意味']}")
    elif st.button('行動・精神的な特性') and st.session_state.selected_word['分類']=='行動・精神的な特性':
        st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
        if st.button('意味を確認する'):
            st.session_state.display_meaning = True

        if st.session_state.display_meaning:
            st.write(f"意味: {st.session_state.selected_word['意味']}")
    elif st.button('自然・現象に関連するもの') and st.session_state.selected_word['分類']=='自然・現象に関連するもの':
        st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
        if st.button('意味を確認する'):
            st.session_state.display_meaning = True

        if st.session_state.display_meaning:
            st.write(f"意味: {st.session_state.selected_word['意味']}")'''