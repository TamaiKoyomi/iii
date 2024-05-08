import streamlit as st

st.title("BMI計算アプリ")

user_height=st.number_input("あなたの身長を入力してください(単位はm)。", min_value=1)
user_weight=st.number_input("あなたの体重を入力してください(単位はkg)。", min_value=1)

a=user_height*user_height
bmi=user_weight/a

if st.button("計算する"):
    st.write("あなたのBMIは"+str(bmi)+"です")

    if bmi<18.5:
        st.write("あなたは低体重(瘦せ型)です")
    elif 18.5<=bmi and bmi<25:
        st.write("あなたは標準体重です")
    elif 25<=bmi and bmi<30:
        st.write("あなたは肥満(1度)です")
    elif 30<=bmi and bmi<35:
        st.write("あなたは肥満(2度)です")
    elif 35<=bmi and bmi<40:
        st.write("あなたは肥満(3度)です")
    else:
        st.write("あなたは肥満(4度)です")

    b=user_height*user_height*22

    st.write("あなたの理想体重は"+str(b)+"kgです")

    if user_weight>b:
        c=user_weight-b
        st.write("理想体重まであと"+str(c)+"kgです")
    elif user_weight<b:
        d=b-user_weight
        st.write("理想体重より"+str(d)+"kg軽いです")
    else:
        st.write("あなたの体重は理想体重ぴったりです")