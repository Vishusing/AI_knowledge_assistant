import streamlit as st

from config.settings import CHROMA_PATH

def render_sidebar():
    with st.sidebar:
        st.markdown("## 📊 Custom Knowledge Assistant")
      
        
        # Better Clear Chat interaction
        if st.button("🧹 Clear Chat", help="Remove all previous conversation history"):
            st.session_state.messages = []
            st.success("Chat history cleared.", icon="✅")
            st.rerun()
        
       
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
        
        return uploaded_pdf