import streamlit as st
st.text("First Page")
if "shared_data" in st.session_state:
        st.write("Shared Data:", st.session_state["shared_data"])