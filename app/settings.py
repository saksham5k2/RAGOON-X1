import os
from app.config import *

# Debugging
DEBUG = True
MAX_PAGES = 10       
PRINT_CHUNKS = False


APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
ENVIRONMENT = os.getenv("ENVIRONMENT")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")
VECTOR_DB_PROVIDER = os.getenv("VECTOR_DB_PROVIDER")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
TOP_K = int(os.getenv("TOP_K"))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))
CHUNK_STRATEGY = os.getenv("CHUNK_STRATEGY")
QDRANT_PATH = os.getenv("QDRANT_PATH")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", 384))
INDEX_BATCH_SIZE = int(os.getenv("INDEX_BATCH_SIZE", 100))
WIKIPEDIA_DUMP = os.getenv("WIKIPEDIA_DUMP")
BM25_INDEX_PATH = os.getenv(
    "BM25_INDEX_PATH",
    "storage/bm25.pkl",
)
RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "BAAI/bge-reranker-base",
)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")
LLM_TEMPERATURE = float(
    os.getenv("LLM_TEMPERATURE", 0)
)

LLM_MAX_TOKENS = int(
    os.getenv("LLM_MAX_TOKENS", 512)
)

DOCUMENT_STORE_PATH = os.getenv(
    "DOCUMENT_STORE_PATH",
    "storage/documents.json",
)