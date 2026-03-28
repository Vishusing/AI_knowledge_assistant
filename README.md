# AI Knowledge Assistant (RAG Application)

> **An easy-to-use tool for asking questions to your own documents using advanced AI.**

---

## What is This App?

The AI Knowledge Assistant is a robust, user-friendly tool that lets you interact with your own PDF documents through a chat interface powered by AI. It uses a technique called **Retrieval Augmented Generation (RAG)**, which means:
- Your documents are read and converted into numerical "vectors" so the AI can understand their content.
- When you ask a question, the system finds and retrieves the most relevant pieces from your documents.
- The AI combines these pieces with its own large language model (LLM) knowledge to generate clear, grounded answers that reference your provided information.

**In short:** You can upload a PDF, then chat with the AI and get informed, document-based answers!

---

## Key Features

- **PDF Upload & Ingestion:** Easily upload PDFs through the browser.
- **Semantic Search:** Search beyond keywords–find meaningfully relevant content.
- **Context-Aware Answers:** The AI uses document context before answering.
- **Cited, Trustworthy Responses:** Answers are supported by your document’s actual text.

---

## How It Works (Architecture)

1. **Document Loader:** Reads and processes your PDF(s).
2. **Embedding Model:** Converts document parts to numerical vectors (meanings).
3. **Vector Database:** Stores these vectors for efficient lookup (ChromaDB).
4. **Retriever:** Finds the most relevant document chunks at question time.
5. **LLM Generator:** The AI answers your question, grounding the answer in what it found.

---

## Getting Started: How to Use

### 1. Prerequisites

- Ensure you have Python installed.
- You need an **OpenRouter API key**. Set `OPENROUTER_API_KEY` in your `.env` file.

### 2. Setup (First Time)

1. **Create and Activate Virtual Environment (Windows PowerShell):**
   ```
   .\venv\Scripts\Activate.ps1
   ```

2. **Install Required Python Packages:**
   ```
   pip install -r requirements.txt
   ```

### 3. Building the Database *(Optional: command-line ingest)*

You can pre-ingest a PDF using:
```
python scripts/build_db.py
```
> - Ensure only one PDF is in the `data/raw/` folder for this script.  
> - To ingest other files or multiple PDFs, use the web app's upload feature directly.

### 4. Launch the App (Streamlit UI)

1. **With your virtual environment still active:**
   ```
   streamlit run streamlit_app.py
   ```
2. **In the web browser:**
    - Upload a PDF via the sidebar.
    - Click "Feed this PDF to the AI".
    - Start chatting! Ask questions and receive answers with supporting context.

---

## Technology Stack

- **Python** (core language)
- **LangChain** (RAG framework)
- **ChromaDB** (vector storage)
- **SentenceTransformers** (text embeddings)
- **OpenRouter LLM** (language model access – via `OPENROUTER_API_KEY`)
- **Streamlit** (interactive web UI for chat and PDF upload)

---

## Planned Enhancements

- REST API with **FastAPI** (for integrations)
- **Chat memory** (keep track of multi-turn conversations)
- Better support for **multiple documents** at once

---

*If you have any questions or ideas, feel free to open an issue or contribute!*
