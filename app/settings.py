import os
from app.config import *

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