from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class CompressionStage(RetrievalStage):

    def __init__(self, compressor):
        self.compressor = compressor

    def run(self, state):

        compressed = self.compressor.compress(
            state["query"],
            state["reranked"],
        )

        state["compressed"] = compressed

        logger.info(
            "Compressed %d chunks.",
            len(compressed),
        )

        return state