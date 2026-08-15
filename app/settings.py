import os

from app.config import *


# ============================================================
# Runtime
# ============================================================

DEBUG = False
MAX_PAGES = 10
PRINT_CHUNKS = False


# ============================================================
# Application
# ============================================================

APP_NAME = os.getenv(
    "APP_NAME",
    "RAGOON-X1",
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "2.0.0",
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "production",
)


# ============================================================
# LLM
# ============================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "groq",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama-3.1-8b-instant",
)

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

GROQ_BASE_URL = os.getenv(
    "GROQ_BASE_URL"
)

LLM_TEMPERATURE = float(
    os.getenv(
        "LLM_TEMPERATURE",
        0,
    )
)

LLM_MAX_TOKENS = int(
    os.getenv(
        "LLM_MAX_TOKENS",
        512,
    )
)


# ============================================================
# Embeddings
# ============================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-small-en-v1.5",
)

EMBEDDING_DIM = int(
    os.getenv(
        "EMBEDDING_DIM",
        384,
    )
)


# ============================================================
# Retrieval
# ============================================================

TOP_K = int(
    os.getenv(
        "TOP_K",
        10,
    )
)


# ============================================================
# Chunking
# ============================================================

CHUNK_SIZE = int(
    os.getenv(
        "CHUNK_SIZE",
        512,
    )
)

CHUNK_OVERLAP = int(
    os.getenv(
        "CHUNK_OVERLAP",
        100,
    )
)

CHUNK_STRATEGY = os.getenv(
    "CHUNK_STRATEGY",
    "recursive",
)


# ============================================================
# Vector Database
# ============================================================

VECTOR_DB_PROVIDER = os.getenv(
    "VECTOR_DB_PROVIDER",
    "qdrant",
)

QDRANT_PATH = os.getenv(
    "QDRANT_PATH",
    "storage/qdrant_store",
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "ragoonx",
)


# ============================================================
# Indexing
# ============================================================

INDEX_BATCH_SIZE = int(
    os.getenv(
        "INDEX_BATCH_SIZE",
        100,
    )
)

BM25_INDEX_PATH = os.getenv(
    "BM25_INDEX_PATH",
    "storage/bm25.pkl",
)


# ============================================================
# Reranking
# ============================================================

RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "BAAI/bge-reranker-base",
)


# ============================================================
# Document Storage
# ============================================================

DOCUMENT_STORE_PATH = os.getenv(
    "DOCUMENT_STORE_PATH",
    "storage/documents.json",
)


# ============================================================
# Legacy / Optional Data Source
# ============================================================

WIKIPEDIA_DUMP = os.getenv(
    "WIKIPEDIA_DUMP"
)