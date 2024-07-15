import streamlit as st

st.title("Test")
stuN = st.text_input("학번 이름")
if st.button("Save"):
    if stuN not in st.session_state :
        st.session_state.stuN = stuN