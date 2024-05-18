import streamlit as st
st.text("Second page")
val = st.text_input("값을 넣으세요")
if st.button("Save"):
    st.session_state["shared_data"] = val