import streamlit as st
import quizes as qz

st.header("Quiz")

colText1,colText2,colText3=st.columns(3)

st.markdown("### **Wie geht es weiter ABC...**")

col1,col2 = st.columns(2)
question= qz.find_allQuestions()
st.write(question)


with col1:
    st.button("Antwort A:", key="s1Aa")
    st.button("Antwort B:", key="s1Ab")
    st.button("Antwort C:", key="s1Ac")

with col2:
    st.button("Antwort A:", key="s2Aa")
    st.button("Antwort B", key="s2Ab")
    st.button("Antwort C", key="s2Ac")
