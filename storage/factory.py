from app.settings import VECTOR_DB_PROVIDER

from storage.qdrant_store import QdrantStore
from storage.bm25_store import BM25Store
from storage.json_document_store import (
    JsonDocumentStore,
)

from app.settings import (
    DOCUMENT_STORE_PATH,
)

class StorageFactory:

    @staticmethod
    def create_vector_store():

        provider = VECTOR_DB_PROVIDER.lower()

        if provider == "qdrant":
            return QdrantStore()

        raise ValueError(
            f"Unsupported vector database: {provider}"
        )

    @staticmethod
    def create_sparse_store():

        return BM25Store()

    @staticmethod
    def create_document_store():

        return JsonDocumentStore(
            DOCUMENT_STORE_PATH
        )

    @staticmethod
    def create_document_store():
        return JsonDocumentStore(
            DOCUMENT_STORE_PATH
        )