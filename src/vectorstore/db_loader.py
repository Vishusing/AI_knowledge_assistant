"""
Vector DB loader

Loads existing database instead of recreating.
"""

from langchain_chroma import Chroma

from config.settings import CHROMA_PATH

from src.embeddings.embedding_model import get_embedding_model


def load_vector_store():
    """
    Load existing vector database.
    """
    print("Loading existing vector DB...")

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    return vectorstore