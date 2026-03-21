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

    If `file_path` is not provided, it will try to ingest the only PDF found in
    `config.settings.DATA_PATH`.
    """
    if file_path is None:
        try:
            pdfs = [
                os.path.join(DATA_PATH, name)
                for name in os.listdir(DATA_PATH)
                if name.lower().endswith(".pdf")
            ]
        except FileNotFoundError:
            pdfs = []

        if len(pdfs) == 1:
            file_path = pdfs[0]
        elif len(pdfs) == 0:
            raise FileNotFoundError(
                f"No PDFs found in `{DATA_PATH}`. "
                f"Upload a PDF via the Streamlit UI or pass `file_path` to `build(file_path=...)`."
            )
        else:
            raise FileNotFoundError(
                f"Multiple PDFs found in `{DATA_PATH}`. "
                f"Pass `file_path` to `build(file_path=...)` to choose which one to ingest."
            )

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