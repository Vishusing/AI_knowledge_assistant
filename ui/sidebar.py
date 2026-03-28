import streamlit as st

from config.settings import CHROMA_PATH
from services.vector_service import database_exists  # <-- import was missing
from scripts.build_db import build  # <-- import was missing

def render_sidebar():
    with st.sidebar:
        # Progress indicators and PDF upload
        uploading = st.session_state.get("upload_pdf_in_progress", False)
        db_building = st.session_state.get("db_building_in_progress", False)
        spinner_message = None

        if uploading:
            spinner_message = "⏫ Uploading PDF... Please wait."
        elif db_building: 
            spinner_message = "🔄 Building vector database..."

        # Use a spinner if things are happening
        if spinner_message:
            with st.spinner(spinner_message):
                uploaded_pdf = st.file_uploader(
                    "📄 Upload PDF",
                    type=["pdf"],
                    disabled=True if db_building else False,
                    key="pdf_upload_spinner"
                )
        else:
            uploaded_pdf = st.file_uploader(
                "📄 Upload PDF",
                type=["pdf"],
                help="Only PDF files are supported (max 1 at a time)",
                key="pdf_upload_normal"
            )
              
        # PDF status message
        if "uploaded_pdf_signature" in st.session_state and st.session_state.uploaded_pdf_signature:
            st.success("PDF uploaded ✔", icon="📄")
        elif uploading or db_building:
            pass
        else:
            st.info("Please upload a PDF file to get started.", icon="ℹ️")

        # Better Clear Chat interaction
        if st.button("🧹 Clear Chat", help="Remove all previous conversation history"):
            st.session_state.messages = []
            st.success("Chat history cleared.", icon="✅")
            st.rerun()

        if not database_exists(CHROMA_PATH):
            st.sidebar.error("Vector DB missing")

        # fix: initialize pdf_path outside if
        pdf_path = st.session_state.get("pdf_path")

        if st.sidebar.button("Feed PDF"):
            if pdf_path:
                build(pdf_path)
                if "db_version" not in st.session_state:
                    st.session_state.db_version = 1
                else:
                    st.session_state.db_version += 1
                st.sidebar.success("Database built")
                st.rerun()
            else:
                st.sidebar.warning("No PDF file found to build database.")

        return uploaded_pdf