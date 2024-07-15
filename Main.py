import streamlit as st

st.header('', divider='rainbow')
st.title('_문소정_ is :blue[cool] :sunglasses:')
st.caption('***저는 :rainbow[문소정] 입니다***')

button = st.button("소개 보기", type="primary")
if button:
    st.write("1-2")