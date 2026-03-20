"""
LLM Module

Purpose:
Connect to language model.
"""

from langchain_openai import ChatOpenAI

import os


def get_llm():

    """
    Loads LLM model.

    Returns:
        LLM object
    """

    print("Loading LLM...")

    llm = ChatOpenAI(

        model="openrouter/auto",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0,   # deterministic answers
    )
    return llm