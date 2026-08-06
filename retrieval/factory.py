from retrieval.dense_retriever import DenseRetriever


class RetrieverFactory:

    @staticmethod
    def create_dense(
        embedding_model,
        vector_store,
    ):
        return DenseRetriever(
            embedding_model,
            vector_store,
        )