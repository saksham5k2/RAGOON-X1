from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class RerankingStage(RetrievalStage):

    def __init__(
        self,
        reranker,
    ):
        self.reranker = reranker

    def run(
        self,
        state,
    ):

        reranked = self.reranker.rerank(
            state["query"],
            state["retrieved"],
            top_k=state["top_k"],
        )

        state["reranked"] = reranked

        logger.info(
            "Returned Top %d reranked chunks.",
            len(reranked),
        )

        return state