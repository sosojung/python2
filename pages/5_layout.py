import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with col2:
   st.header("Hello")

with col3:
   st.header("Bye")

   #메인 페이지
   #학번 이름 입력
   #/test
   #주관식 1문제 간단하게 하고
   #레이아웃써서 객관식 5지선다 내고
   #/result
   #누구 몇점인지 띄우기