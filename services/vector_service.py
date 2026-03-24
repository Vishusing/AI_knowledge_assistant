import os
import streamlit as st

from src.vectorstore.db_loader import load_vector_store
from src.retriever.retriever import create_retriever

@st.cache_resource(show_spinner=False)
def get_retriever(version):

    vectorstore=load_vector_store()

    return create_retriever(vectorstore)


def database_exists(path):

    return os.path.exists(path)