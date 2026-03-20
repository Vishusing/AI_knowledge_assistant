"""
Build vector database

Run only once unless documents change.
"""

from src.loaders.ingest import ingest_document

from src.embeddings.embedder import generate_embeddings

from src.vectorstore.chroma_store import create_vector_store


def build():

    file_path = "data/raw/sample.pdf"

    chunks = ingest_document(file_path)

    embedding_model, chunks = generate_embeddings(chunks)

    create_vector_store(

        chunks,
        embedding_model

    )

    print("\nDatabase built successfully")


if __name__ == "__main__":

    build()