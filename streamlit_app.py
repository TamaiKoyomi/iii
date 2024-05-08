import streamlit as st

st.title("BMI計算アプリ")

user_height=st.number_input("あなたの身長を入力してください(単位はm)。")
user_weight=st.number_input("あなたの体重を入力してください(単位はkg)。")

a=user_weight/user_height/user_height

st.write("あなたのBMIは"+str(a)+"です")