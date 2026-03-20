# Central configuration file
# All constants stored here

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Vector DB settings
CHROMA_PATH = "chroma_db"

# Data path
DATA_PATH = "data/raw"

# Chunk settings (important for RAG quality)
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50