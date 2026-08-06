from retrieval.hybrid.fusion import ReciprocalRankFusion


class HybridRetriever:

    def __init__(
        self,
        dense_retriever,
        sparse_store,
    ):

        self.dense = dense_retriever

        self.sparse = sparse_store

        self.fusion = ReciprocalRankFusion()

    def retrieve(
        self,
        query,
        top_k=10,
    ):

        dense_results = self.dense.retrieve(
            query=query,
            top_k=top_k,
        )

        sparse_results = self.sparse.search(
            query=query,
            limit=top_k,
        )

        return self.fusion.fuse(
            dense_results,
            sparse_results,
        )[:top_k]