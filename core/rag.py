from src.llm.generator import generate_answer

def ask_question(retriever,prompt):

    answer=generate_answer(
        retriever,
        prompt
    )

    return answer