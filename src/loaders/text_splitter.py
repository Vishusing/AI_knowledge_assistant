"""
Text Splitter Module

Purpose:
Split documents into chunks suitable for embeddings.

Chunking improves retrieval accuracy.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import CHUNK_SIZE
from config.settings import CHUNK_OVERLAP


def split_documents(documents):

    """
    Split documents into chunks.

    Args:
        documents : loaded PDF documents

    Returns:
        chunks : smaller text pieces
    """

    print("Splitting documents into chunks...")

    # Recursive splitter preserves context better
    text_splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,        # Size of each chunk
        chunk_overlap=CHUNK_OVERLAP   # Overlap keeps context continuity

    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks