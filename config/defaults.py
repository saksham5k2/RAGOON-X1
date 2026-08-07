DEFAULT_CONFIG = {
    "llm": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile",
    },
    "embedding": {
        "provider": "sentence-transformers",
        "model": "BAAI/bge-small-en-v1.5",
    },
    "retrieval": {
        "top_k": 10,
        "rewrite": True,
        "multi_query": True,
        "rerank": True,
        "compress": True,
    },
    "chunking": {
        "strategy": "recursive",
        "chunk_size": 750,
        "overlap": 150,
    },
    "storage": {
        "provider": "qdrant",
        "path": "./db",
    },
    "data": {
        "source": "./documents",
    },
}