"""
Document Ingestion Pipeline

This connects:
Loader + Splitter

Creates ready to embed chunks.
"""

from src.loaders.pdf_loader import load_pdf
from src.loaders.text_splitter import split_documents


def ingest_document(file_path):

    """
    Full ingestion pipeline.

    PDF → Documents → Chunks

    Returns:
        chunks ready for embeddings
    """

    # Step 1 load PDF
    documents = load_pdf(file_path)

    # Step 2 split into chunks
    chunks = split_documents(documents)

    return chunks