"""
Answer generation module
Connects:
Retriever + LLM + Prompt
"""

from src.retriever.query import get_context
from src.llm.llm_model import get_llm
from src.llm.prompt import get_prompt

def generate_answer(retriever, query):
    """
    Generate RAG answer.
    Steps:
    1 retrieve context
    2 build prompt
    3 call LLM
    """

    print("Generating answer...")

    context = get_context
        retriever,
        query
    )

    # Load prompt
    prompt = get_prompt()

    # Format prompt
    formatted_prompt = prompt.format(
        context=context,
        question=query
    )

    # Load LLM
    llm = get_llm()

    # Generate response
    response = llm.invoke(
        formatted_prompt
    )

    return response.content