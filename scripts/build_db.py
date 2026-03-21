"""
Build vector database

Run only once unless documents change.
"""

import os
from typing import Optional

from config.settings import DATA_PATH

from src.loaders.ingest import ingest_document

from src.embeddings.embedder import generate_embeddings

from src.vectorstore.chroma_store import create_vector_store


def build(file_path: Optional[str] = None):
    """
    Build the Chroma vector database.

    By default it ingests `data/raw/sample.pdf` (via `config.settings.DATA_PATH`).
    """
    if file_path is None:
        file_path = os.path.join(DATA_PATH, "sample.pdf")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF not found at: {file_path}")

    chunks = ingest_document(file_path)

    embedding_model, chunks = generate_embeddings(chunks)

    create_vector_store(

        chunks,
        embedding_model

    )

    print("\nDatabase built successfully")


if __name__ == "__main__":

    build()