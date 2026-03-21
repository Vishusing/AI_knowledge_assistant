"""
Embedding Model Module
Purpose:
Convert text chunks into vector embeddings.
This enables semantic search.
"""

from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import EMBEDDING_MODEL


def get_embedding_model():
    """
    Loads embedding model.
    Returns:
        embedding model object
    """
    print("Loading embedding model...")

    # Load sentence transformer model
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    print("Embedding model loaded")

    return embeddings