import os
import hashlib

import streamlit as st

from config.settings import CHROMA_PATH, DATA_PATH
from scripts.build_db import build
from src.llm.generator import generate_answer
from src.retriever.retriever import create_retriever
from src.vectorstore.db_loader import load_vector_store


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_ROOT)  # Ensure relative paths in config/settings resolve correctly.

st.set_page_config(page_title="AI Knowledge Assistant", layout="centered")

st.title("AI Knowledge Assistant")
st.caption("Retrieval-Augmented Generation (RAG) over your document database.")


if not os.getenv("OPENROUTER_API_KEY"):
    st.warning(
        "Environment variable `OPENROUTER_API_KEY` is not set. "
        "Set it in your `.env` file before asking questions."
    )


if "db_version" not in st.session_state:
    # Increment this to force cached resources (retriever/vectorstore) to reload.
    st.session_state.db_version = 0

if "messages" not in st.session_state:
    # Simple chat history storage for the UI.
    st.session_state.messages = []

if "uploaded_pdf_signature" not in st.session_state:
    # Tracks last uploaded file to avoid re-saving on Streamlit reruns.
    st.session_state.uploaded_pdf_signature = None


@st.cache_resource(show_spinner=False)
def get_retriever(db_version: int):
    # db_version isn't used directly; it's only there to invalidate the cache.
    _ = db_version
    vectorstore = load_vector_store()
    return create_retriever(vectorstore)


def database_exists() -> bool:
    # Chroma uses a persistence directory; if it exists, assume DB is available.
    return os.path.exists(CHROMA_PATH)


st.sidebar.header("Vector database")
st.sidebar.write(f"Chroma path: `{CHROMA_PATH}`")

if st.sidebar.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

uploaded_pdf = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"],
    key="uploaded_pdf",
)

if uploaded_pdf is not None:
    file_bytes = uploaded_pdf.getvalue()
    uploaded_signature = (
        f"{uploaded_pdf.name}:{uploaded_pdf.size}:"
        f"{hashlib.sha256(file_bytes).hexdigest()}"
    )

    if uploaded_signature != st.session_state.uploaded_pdf_signature:
        # Persist uploaded PDF as the single source file for ingestion.
        os.makedirs(DATA_PATH, exist_ok=True)
        for name in os.listdir(DATA_PATH):
            existing_path = os.path.join(DATA_PATH, name)
            if os.path.isfile(existing_path) and name.lower().endswith(".pdf"):
                os.remove(existing_path)

        filename = uploaded_pdf.name
        uploaded_path = os.path.join(DATA_PATH, filename)
        with open(uploaded_path, "wb") as f:
            f.write(file_bytes)

        st.session_state["pdf_path"] = uploaded_path
        st.session_state.uploaded_pdf_signature = uploaded_signature
        st.sidebar.success(f"Uploaded: `{uploaded_pdf.name}`")

pdf_path = st.session_state.get("pdf_path")

needs_build = not database_exists()

if needs_build:
    st.sidebar.error("Vector DB not found. Build it before asking questions.")

build_clicked = st.sidebar.button("Feed this PDF to the AI")

if build_clicked:
    with st.sidebar.spinner("Building vector database..."):
        try:
            if not pdf_path:
                st.sidebar.error("Upload a PDF first, then click the build button.")
                st.stop()

            build(pdf_path)
            st.session_state.db_version += 1
            st.sidebar.success("Database built. You can ask questions now.")
        except Exception as e:
            st.sidebar.error(f"Failed to build database: {e}")

    # Ensure the UI refreshes after cache invalidation.
    st.rerun()


retriever = None
if database_exists():
    with st.spinner("Loading retriever..."):
        retriever = get_retriever(st.session_state.db_version)


# Render chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Question and answer logic starts here
prompt = st.chat_input("Ask a question")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not retriever:
        st.error("Vector DB is not available yet. Build it using the sidebar.")
    elif not os.getenv("OPENROUTER_API_KEY"):
        st.error("Missing `OPENROUTER_API_KEY` environment variable.")
    else:
        with st.spinner("Generating answer..."):
            try:
                answer = generate_answer(retriever, prompt)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
                st.chat_message("assistant").write(answer)
            except Exception as e:
                st.error(f"Failed to generate answer: {e}")

