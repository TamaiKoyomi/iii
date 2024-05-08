import streamlit as st

st.title("BMI計算アプリ")

user_height=st.number_input("あなたの身長を入力してください(単位はm)。", min_value=1)
user_weight=st.number_input("あなたの体重を入力してください(単位はkg)。", min_value=1)

a=user_height*user_height
bmi=user_weight/a

st.write("あなたのBMIは"+str(bmi)+"です")

b=user_height*user_height*22

st.write("あなたの理想体重は"+str(b)+"です")

if user_weight>b:
    c=user_weight-b
    st.write("理想体重まであと"+str(c)+"kgです")
elif user_weight<b:
    d=b-user_weight
    st.write("理想体重より"+str(d)+"kg軽いです")
else:
    st.write("あなたの体重は理想体重ぴったりです")