"""
Embedding pipeline

Connects:
Chunks → Embeddings
"""

from src.embeddings.embedding_model import get_embedding_model


def generate_embeddings(chunks):

    """
    Generate embeddings for chunks.

    Returns:
        embedding model + chunks
    """

    print("Generating embeddings...")

    embedding_model = get_embedding_model()

    # Note:
    # Vector DB will generate embeddings automatically
    # So we just return model + chunks

    return embedding_model, chunks