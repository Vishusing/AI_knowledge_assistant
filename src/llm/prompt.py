"""
Prompt template for RAG
"""

from langchain_core.prompts import PromptTemplate

def get_prompt():

    template = """

You are an AI Knowledge Assistant.

Answer ONLY from the provided context.

If answer not in context say:
"I don't find this in the document"

Context:
{context}

Question:
{question}

Answer:

"""

    prompt = PromptTemplate(

        template=template,

        input_variables=["context","question"]

    )

    return prompt