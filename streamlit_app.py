import streamlit as st
import pandas as pd
import numpy as np

if 'user_name' not in st.session_state:
    st.session_state.user_name=''

if 'team_name' not in st.session_state:
    st.session_state.team_name=''

if 'page' not in st.session_state:
    st.session_state.page='input'

def show_name_input():
    st.title('初期設定')

    # 名前と所属チームの入力フォーム
    with st.form(key='input_form'):
        user_name = st.text_input('名前を入力してください。')
        st.write('所属チームを選択してください。')
        if st.button('a'):
            st.session_state.team_name = 'a'
        if st.button('b'):
            st.session_state.team_name='a'
        submit_button = st.form_submit_button('ゲームを開始する！')

        if submit_button:
            if st.session_state.user_name and st.session_state.team_name:
                # セッションステートに保存
                st.session_state.user_name = user_name
                # ページをゲーム画面に切り替える
                st.session_state.page = 'game'
            else:
                st.error('名前を入力し、所属チームを選択してください。')

def show_game():
    st.title('四字熟語カテゴリークイズ')
    st.write(st.session_state.user_name + 'さんは、' + st.session_state.team_name + 'に所属しています。')
    st.write('aとbに分かれてクイズの正答率を競争します。最も正しいと思うものを選んでください。しかし、ChatGPTが分類したものなので違うと思っても怒らないでください。')

    # Load the data
    @st.cache
    def load_data():
        return pd.read_excel("四字熟語ガチャ.xlsx")

    words_df = load_data()

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

show_game()

