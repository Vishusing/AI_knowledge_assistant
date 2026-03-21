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

Prerequisite:
- Ensure `OPENROUTER_API_KEY` is set in `.env`.

Build database (optional):

1. Activate the virtual environment (Windows PowerShell):
   `.\venv\Scripts\Activate.ps1`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Build the database (optional):
   `python scripts/build_db.py`

Note: `scripts/build_db.py` ingests the single PDF found in `data/raw/`. If there are none (or multiple), it raises an error; use the Streamlit upload flow instead.

Streamlit UI:

1. (With the venv still active) Start the app:
   `streamlit run streamlit_app.py`

2. Upload a PDF in the sidebar, click `Feed this PDF to the AI`, then ask questions in the chat.

## Tech Stack

Python
LangChain
ChromaDB
SentenceTransformers
OpenRouter LLM (`OPENROUTER_API_KEY` in `.env`)
Streamlit UI (chat + PDF upload)

## Future Improvements

FastAPI API
Chat memory
Multi-document ingestion