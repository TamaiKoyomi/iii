import streamlit as st
import pandas as pd
import numpy as np

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

def show_game():
    st.title('四字熟語カテゴリークイズ')
    st.write('四字熟語のカテゴリーについて、最も正しいと思うものを選んでください。ただ、ChatGPTが分類したものなので違うと思っても怒らないでください。')

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
            if judge('文学・哲学的なテーマ性'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")


        elif st.button('行動・精神的な特性'):
            if judge('行動・精神的な特性'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")

        elif st.button('自然・現象に関連するもの'):
            if judge('自然・現象に関連するもの'):
                st.write('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.write('残念、不正解です。')
                st.write(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.write('正しい答えを確認し、この熟語をマスターしましょう！')
                st.write(f"この熟語の意味: {st.session_state.selected_word['意味']}")

def show_pro():
    st.title('カテゴリー別一覧表')

    tab = st.radio('どのカテゴリーを見ますか？',['文学・哲学的なテーマ性','行動・精神的な特性','自然・現象に関連するもの'])

    filtered_df = words_df[words_df['分類'] == tab]

    for index,row in filtered_df.iterrows():
        st.subheader(f"単語名:{row['単語']}")
        st.write(f"読み方:{row['読み方']}")
        st.write(f"意味:{row['意味']}")

def game_yomi():
    st.title('読み方クイズ')
    st.write('表示される四字熟語の読みを当ててください。ヒントとして意味を確認することができます。また、全角ひらがなでの解答お願いします。')

    if st.button('クイズを解く'):
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

    st.subheader(f"単語名:{st.session_state.selected_word['単語']}")
    answer = st.text_input('読み方を入力してください:')

    if st.button('解答する'):
        if answer == st.session_state.selected_word['読み方']:
                st.success('おめでとうございます、正解です！')
        else:
            st.error('違います。答えを確認してください')
            st.error(f"答え:{st.session_state.selected_word['読み方']}")
    if st.button('ヒントを見る'):
        st.write(f"この単語の意味:{st.session_state.selected_word['意味']}")

def menu():
    st.title('四字熟語クイズ')
    st.write('四字熟語に関するクイズをつくりました。好きなクイズで遊んでください！')
    menu_tab = st.radio('選択してください',['カテゴリークイズ','読み方クイズ','カテゴリー別一覧'])
    if menu_tab == 'カテゴリークイズ':
        show_game()
    elif menu_tab == '読み方クイズ':
        game_yomi()
    elif menu_tab == 'カテゴリー別一覧':
        show_pro()

sidetab = st.sidebar.radio('選択してください',['メニュー','カテゴリークイズ','読み方クイズ','カテゴリー別一覧'])

if sidetab == 'カテゴリークイズ':
    show_game()
elif sidetab == '読み方クイズ':
    game_yomi()
elif sidetab == 'カテゴリー別一覧':
    show_pro()
elif sidetab == 'メニュー':
    menu()