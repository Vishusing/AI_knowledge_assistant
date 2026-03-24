import os
import streamlit as st

from core.state import init_state
from core.rag import ask_question

from services.vector_service import (
    get_retriever,
    database_exists
)

from services.pdf_service import save_uploaded_pdf

from ui.sidebar import render_sidebar
from ui.chat import (
    render_messages,
    add_user_message,
    add_ai_message
)

from config.settings import CHROMA_PATH
from scripts.build_db import build


st.set_page_config(
    page_title="AI Knowledge Assistant"
)

st.title("AI Knowledge Assistant")

init_state()

uploaded_pdf=render_sidebar()

if uploaded_pdf:

    path=save_uploaded_pdf(
        uploaded_pdf
    )

    if path:

        st.session_state["pdf_path"]=path

        st.sidebar.success("Uploaded")


if not database_exists(CHROMA_PATH):

    st.sidebar.error(
        "Vector DB missing"
    )


if st.sidebar.button(
    "Feed PDF"
):

    pdf_path=st.session_state.get(
        "pdf_path"
    )

    if pdf_path:

        build(pdf_path)

        st.session_state.db_version+=1

        st.sidebar.success(
            "Database built"
        )

        st.rerun()


retriever=None

if database_exists(CHROMA_PATH):

    retriever=get_retriever(

        st.session_state.db_version

    )


render_messages()

prompt=st.chat_input(
    "Ask question"
)

if prompt:

    add_user_message(prompt)

    st.chat_message(
        "user"
    ).write(prompt)

    if not retriever:

        st.error("Build DB first")

    else:

        with st.spinner(
            "Thinking..."
        ):

            answer=ask_question(
                retriever,
                prompt
            )

            add_ai_message(answer)

            st.chat_message(
                "assistant"
            ).write(answer)