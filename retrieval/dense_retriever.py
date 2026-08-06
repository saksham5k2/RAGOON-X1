from retrieval.base import BaseRetriever


class DenseRetriever(BaseRetriever):

    def __init__(
        self,
        embedding_model,
        vector_store,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
    ):

        query_embedding = self.embedding_model.embed_query(
            query
        )

        return self.vector_store.search(
            query_embedding,
            limit=top_k,
        )