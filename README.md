# AI Knowledge Assistant (RAG Application)

## Overview

AI Knowledge assistant built using:

Python
LangChain
ChromaDB
Sentence Transformers
LLM

The system follows a Retrieval Augmented Generation (RAG) pipeline where documents are processed, stored as vectors, retrieved based on queries, and used by an LLM to generate grounded responses.

## Features

PDF ingestion
Semantic search
Context retrieval
Grounded answer generation

## Architecture

Document Loader
Embedding Model
Vector Database
Retriever
LLM Generator

## Run Project

Build database:

1. Activate the virtual environment (Windows PowerShell):
   `.\venv\Scripts\Activate.ps1`

2. Build the database:
   `python scripts/build_db.py`

Ask questions:

1. (With the venv still active) Ask questions:
   `python scripts/ask.py`

## Tech Stack

Python
LangChain
ChromaDB
SentenceTransformers
OpenAI/Groq or any other LLM (Just paste API key of that LLM in .env to use it)

## Future Improvements

Streamlit UI
FastAPI API
Chat memory
Multi-document ingestion