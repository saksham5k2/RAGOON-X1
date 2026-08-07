from dataclasses import dataclass


@dataclass
class LLMConfig:
    provider: str
    model: str
    api_key: str


@dataclass
class EmbeddingConfig:
    provider: str
    model: str


@dataclass
class RetrievalConfig:
    top_k: int
    rewrite: bool
    multi_query: bool
    rerank: bool
    compress: bool


@dataclass
class ChunkingConfig:
    strategy: str
    chunk_size: int
    overlap: int


@dataclass
class StorageConfig:
    provider: str
    path: str


@dataclass
class DataConfig:
    source: str


@dataclass
class RagoonConfig:
    llm: LLMConfig
    embedding: EmbeddingConfig
    retrieval: RetrievalConfig
    chunking: ChunkingConfig
    storage: StorageConfig
    data: DataConfig