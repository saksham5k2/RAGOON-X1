from retrieval.stages.base import RetrievalStage


class CompressionStage(RetrievalStage):

    def __init__(self, compressor):
        self.compressor = compressor

    def run(self, state):

        compressed = self.compressor.compress(
            state["reranked"]
        )

        state["compressed"] = compressed

        return state