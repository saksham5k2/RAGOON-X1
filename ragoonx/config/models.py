from dataclasses import dataclass


@dataclass
class LLMConfig:
    provider: str
    model: str
    api_key: str = ""
    base_url: str = ""
    temperature: float = 0.0
    max_tokens: int = 512


@dataclass
class EmbeddingConfig:
    provider: str
    model: str


@dataclass
class RetrievalConfig:
    top_k: int = 10


@dataclass
class ChunkingConfig:
    strategy: str = "recursive"
    size: int = 512
    overlap: int = 100


@dataclass
class StorageConfig:
    provider: str = "qdrant"
    qdrant_path: str = "storage/qdrant_store"
    bm25_path: str = "storage/bm25.pkl"
    document_store: str = "storage/documents.json"


@dataclass
class DataConfig:
    wikipedia_dump: str = ""


@dataclass
class RagoonConfig:
    llm: LLMConfig
    embedding: EmbeddingConfig
    retrieval: RetrievalConfig
    chunking: ChunkingConfig
    storage: StorageConfig
    data: DataConfig