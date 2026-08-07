import app.settings as settings


class ConfigSynchronizer:

    @staticmethod
    def synchronize(config):

        settings.LLM_PROVIDER = config.llm.provider
        settings.LLM_MODEL = config.llm.model
        settings.GROQ_API_KEY = config.llm.api_key
        settings.GROQ_BASE_URL = config.llm.base_url
        settings.LLM_TEMPERATURE = config.llm.temperature
        settings.LLM_MAX_TOKENS = config.llm.max_tokens

        settings.EMBEDDING_MODEL = (
            config.embedding.model
        )

        settings.TOP_K = (
            config.retrieval.top_k
        )

        settings.CHUNK_SIZE = (
            config.chunking.size
        )

        settings.CHUNK_OVERLAP = (
            config.chunking.overlap
        )

        settings.CHUNK_STRATEGY = (
            config.chunking.strategy
        )

        settings.QDRANT_PATH = (
            config.storage.qdrant_path
        )

        settings.BM25_INDEX_PATH = (
            config.storage.bm25_path
        )

        settings.DOCUMENT_STORE_PATH = (
            config.storage.document_store
        )

        settings.WIKIPEDIA_DUMP = (
            config.data.wikipedia_dump
        )