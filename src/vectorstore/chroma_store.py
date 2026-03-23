"""
Chroma Vector Store Module

Purpose:
Store document embeddings and allow similarity search.
"""

from langchain_community.vectorstores import Chroma

from config.settings import CHROMA_PATH


def create_vector_store(chunks, embedding_model):
    """
    Create and store embeddings in ChromaDB.

    Args:
        chunks : document chunks
        embedding_model : embedding model

    Returns:
        vector database
    """

    print("Creating vector database...")

    # Create Chroma database
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    print("Vector database created")

    return vectorstore