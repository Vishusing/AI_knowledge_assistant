"""
Retriever Module

Purpose:
Convert vector DB into retriever.

Retriever fetches relevant chunks.
"""

def create_retriever(vectorstore):

    """
    Creates retriever from vector DB.

    Args:
        vectorstore : Chroma DB

    Returns:
        retriever object
    """

    print("Creating retriever...")

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,  # number of chunks to retrieve
        },
    )

    print("Retriever ready")

    return retriever