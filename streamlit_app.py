import streamlit as st
import pandas as pd
import numpy as np

global collect_pro,all_pro
all_pro = 0
collect_pro = 0

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

def show_game():
    st.title('四字熟語カテゴリークイズ')
    st.write('四字熟語のカテゴリーについて、最も正しいと思うものを選んでください。けれどChatGPTが分類したものなので違うと思っても怒らないでください。')

    def judge(kategori):
        if st.session_state.selected_word['分類']==kategori:
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

        if st.button('文学・哲学的なテーマ性'):
            global collect_pro,all_pro
            if judge('文学・哲学的なテーマ性'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                collect_pro += 1
                all_pro += 1
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                all_pro += 1


        elif st.button('行動・精神的な特性'):
            global collect_pro,all_pro
            if judge('行動・精神的な特性'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                collect_pro += 1
                all_pro += 1
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                all_pro += 1


        elif st.button('自然・現象に関連するもの'):
            global collect_pro,all_pro
            if judge('自然・現象に関連するもの'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                collect_pro += 1
                all_pro += 1
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
                all_pro += 1

def show_pro():

    tab = st.radio('どのカテゴリーを見ますか？',['文学・哲学的なテーマ性','行動・精神的な特性','自然・現象に関連するもの'])

    filtered_df = words_df[words_df['分類'] == tab]

    for index,row in filtered_df.iterrows():
        st.subheader(f"単語名:{row['単語']}")
        st.write(f"読み方:{row['読み方']}")
        st.write(f"意味:{row['意味']}")

sidetab = st.sidebar.radio('選択してください',['クイズを解く','カテゴリー別一覧を見る'])

if sidetab == 'クイズを解く':
    show_game()
elif sidetab == 'カテゴリー別一覧を見る':
    show_pro()

if all_pro != 0:
    per = collect_pro / all_pro * 100
    st.sidebar.write(f"あなたの正答率は{per:.2f}%です。")
