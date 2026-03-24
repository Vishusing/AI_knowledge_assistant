import os
import hashlib
import streamlit as st

from config.settings import DATA_PATH

def save_uploaded_pdf(uploaded_pdf):

    file_bytes=uploaded_pdf.getvalue()

    signature=f"{uploaded_pdf.name}:{uploaded_pdf.size}:{hashlib.sha256(file_bytes).hexdigest()}"

    if signature==st.session_state.uploaded_pdf_signature:
        return None

    os.makedirs(DATA_PATH,exist_ok=True)

    for name in os.listdir(DATA_PATH):

        path=os.path.join(DATA_PATH,name)

        if os.path.isfile(path) and name.endswith(".pdf"):

            os.remove(path)

    file_path=os.path.join(DATA_PATH,uploaded_pdf.name)

    with open(file_path,"wb") as f:

        f.write(file_bytes)

    st.session_state.uploaded_pdf_signature=signature

    return file_path