import streamlit as st
import pandas as pd
import numpy as np
import random

# Load the data
@st.cache
def load_data():
    return pd.read_excel("四字熟語ガチャ.xlsx")

words_df = load_data()

def decide():
    if st.button('クイズを解く！'):
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

def yojiyoji():
    if 'ans' not in st.session_state:
        yoji_list = list(st.session_state.selected_word['単語'])
        return yoji_list
    else:
        return []

def ranran():
    if 'ans' not in st.session_state:
        yoji_list = yojiyoji()
        if yoji_list:
            ran_list = random.sample(yoji_list,len(yoji_list))
            return ran_list
        else:
            return[]
    else:
        return []

def show_game():
    st.title('四字熟語カテゴリークイズ')
    st.write('四字熟語のカテゴリーについて、最も正しいと思うものを選んでください。なお、これはChatGPTが分類したものです。')

    def judge(kategori):
        if st.session_state.selected_word['分類']==kategori:
            return True
        else:
            return False
     
    decide()

    if 'selected_word' in st.session_state:
        st.header(f"単語名: {st.session_state.selected_word['単語']}")
        st.subheader(f"読み方：{st.session_state.selected_word['読み方']}")

        if st.button('文学・哲学的なテーマ性'):
            if judge('文学・哲学的なテーマ性'):
                st.success('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.success(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.error('残念、不正解です。')
                st.error(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.error('正しい答えを確認し、この熟語をマスターしましょう！')
                st.error(f"この熟語の意味: {st.session_state.selected_word['意味']}")


        elif st.button('行動・精神的な特性'):
            if judge('行動・精神的な特性'):
                st.success('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.success(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.error('残念、不正解です。')
                st.error(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.error('正しい答えを確認し、この熟語をマスターしましょう！')
                st.error(f"この熟語の意味: {st.session_state.selected_word['意味']}")

        elif st.button('自然・現象に関連するもの'):
            if judge('自然・現象に関連するもの'):
                st.success('正解です。おめでとうございます！正確な意味も確認しましょう。')
                st.success(f"この熟語の意味: {st.session_state.selected_word['意味']}")
            else:
                st.error('残念、不正解です。')
                st.error(f"正解はこちら：{st.session_state.selected_word['分類']}")
                st.error('正しい答えを確認し、この熟語をマスターしましょう！')
                st.error(f"この熟語の意味: {st.session_state.selected_word['意味']}")

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

    decide()

    if 'selected_word' in st.session_state:
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
    st.write('四字熟語に関するクイズをつくりました。好きなクイズを選んで遊んでください！')

def ans_pro():
    st.title('熟語クイズ')
    st.write('表示される意味に対応する四字熟語を答えてください。また、漢字四字で答えるようにしてください。表記ゆれにより不正解とされる場合もあるため、不正解と出たら他の表記法で試してみてください。')
    
    decide()

    if 'selected_word' in st.session_state:
        st.subheader(f"四字熟語の意味:{st.session_state.selected_word['意味']}")
        yoji = st.text_input('これは何という四字熟語でしょう？:')

    if st.button('解答する'):
        if yoji == st.session_state.selected_word['単語']:
                st.success('おめでとうございます、正解です！')
        else:
            st.error('違います。')
    if st.button('答えを確認する'):
        st.error(f"答え:{st.session_state.selected_word['単語']}")

def ang_pro():
    st.title('アナグラムクイズ')
    st.write('今から表示される漢字四字を、意味の通りになるように順番にボタンをタップしてください。')

    decide()

    if 'selected_word' in st.session_state:

        if 'ans' not in st.session_state:
            st.session_state.ans = []

        yoji_list = yojiyoji()
        ran_list = ranran()

        if ran_list:
            
            st.subheader(f"四字熟語の意味:{st.session_state.selected_word['意味']}")

            col1,col2,col3,col4,col5 = st.columns(5)

            with col1:
                if st.button(ran_list[0]):
                    st.session_state.ans.append(ran_list[0])
            with col2:
                if st.button(ran_list[1]):
                    st.session_state.ans.append(ran_list[1])
            with col3:
                if st.button(ran_list[2]):
                    st.session_state.ans.append(ran_list[2])
            with col4:
                if st.button(ran_list[3]):
                    st.session_state.ans.append(ran_list[3])
            with col5:
                if st.button('一字消去'):
                    if 'ans' in st.session_state and st.session_state.ans:
                        st.session_state.ans.pop()
    
            st.write(st.session_state.ans)

        else:
            st.write('「クイズを解く！」ボタンを押して、さっそくクイズを解いてみましょう！')

    else:
        st.write('「クイズを解く！」ボタンを押して、さっそくクイズを解いてみましょう！')

sidetab = st.sidebar.radio('選択してください',['メニュー','熟語クイズ','読み方クイズ','カテゴリークイズ','アナグラムクイズ','カテゴリー別一覧']！)

if sidetab == 'カテゴリークイズ':
    show_game()
elif sidetab == '読み方クイズ':
    game_yomi()
elif sidetab == 'カテゴリー別一覧':
    show_pro()
elif sidetab == 'メニュー':
    menu()
elif sidetab == '熟語クイズ':
    ans_pro()
elif sidetab == 'アナグラムクイズ':
    ang_pro()
