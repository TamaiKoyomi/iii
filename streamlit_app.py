import streamlit as st
import random

st.title("おみくじアプリ")

if st.button("おみくじを引く"):
    results=["大吉","中吉","小吉","吉","凶","大凶"]
    result=random.choice(results)

comments={
    "大吉":"素晴らしい一日になりそうです！",
    "中吉":"良いことがあるかもしれません。",
    "小吉":"悪くはなさそうですね。",
    "吉":"まあまあの一日になりそうです。",
    "凶":"注意して過ごしてください。",
    "大凶":"今日は特に注意が必要です！"
}

    if user_name:
        st.write(f"{user_name}さんの結果:{result}")
    else:
        st.write(f"結果:{result}")

    st.write(comments[result])