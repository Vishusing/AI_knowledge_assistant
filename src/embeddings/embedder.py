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

    return embedding_model, chunks