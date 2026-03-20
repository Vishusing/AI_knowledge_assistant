"""
Query the RAG assistant
"""

from src.vectorstore.db_loader import load_vector_store

from src.retriever.retriever import create_retriever

from src.llm.generator import generate_answer


def ask():

    vectorstore = load_vector_store()

    retriever = create_retriever(

        vectorstore

    )

    while True:

        query = input("\nAsk question (or exit): ")

        if query == "exit":

            break

        answer = generate_answer(

            retriever,
            query

        )

        print("\nAnswer:\n")

        print(answer)


if __name__ == "__main__":

    ask()