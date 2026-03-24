import streamlit as st

def init_state():

    if "db_version" not in st.session_state:
        st.session_state.db_version=0

    if "messages" not in st.session_state:
        st.session_state.messages=[]

    if "uploaded_pdf_signature" not in st.session_state:
        st.session_state.uploaded_pdf_signature=None