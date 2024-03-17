import streamlit as st

st.header("contact me")


with st.form(key="my form"):
    useer_email = st.text_input("Your Email Address")
    message = st.text_area("your Message ")
    button = st.form_submit_button("submit")






