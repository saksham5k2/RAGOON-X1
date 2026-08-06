from retrieval.stages.base import RetrievalStage


class RerankingStage(RetrievalStage):

    def __init__(self, reranker):
        self.reranker = reranker

    def run(self, state):

        reranked = self.reranker.rerank(
            query=state["rewritten_query"],
            results=state["fused"],
            top_k=state["top_k"],
        )

        state["reranked"] = reranked

        return state