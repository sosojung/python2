import streamlit as st

st.text("1. 다음 16진수를 8진수로 바꾸시오.")
st.text("abcdef(16)")
ans = st.text_input("답란")
if ans not in st.session_state:
    st.session_state['ans'] = ans