"""
PDF Loader Module

Purpose:
Load PDF documents and convert them into LangChain document objects.

This is the FIRST stage of RAG pipeline.
"""

# Import PDF loader from LangChain
from langchain_community.document_loaders import PyPDFLoader

# Import config values
from config.settings import DATA_PATH


def load_pdf(file_path):
    """
    Loads a PDF file.

    Args:
        file_path (str): path of PDF file

    Returns:
        documents (list): list of document pages
    """

    print("Loading PDF...")

    # PyPDFLoader reads PDF page by page
    loader = PyPDFLoader(file_path)

    # Load document
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents