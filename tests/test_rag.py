"""
Basic pipeline test
"""

from src.vectorstore.db_loader import load_vector_store


def test_db():

    db = load_vector_store()

    assert db is not None

    print("DB test passed")


if __name__ == "__main__":

    test_db()