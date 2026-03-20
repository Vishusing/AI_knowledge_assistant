"""
Query helper

Fetch relevant context.
"""

def get_context(retriever, query):

    """
    Fetch relevant chunks.

    Returns:
        combined context text
    """

    docs = retriever.invoke(

        query

    )

    context = "\n\n".join(

        doc.page_content for doc in docs

    )

    return context