from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class FusionStage(RetrievalStage):

    def __init__(
        self,
        fusion_algorithm,
    ):
        self.fusion_algorithm = fusion_algorithm

    def run(
        self,
        state,
    ):

        fused = self.fusion_algorithm.fuse(
            state["retrieved_lists"]
        )

        state["retrieved"] = fused

        logger.info(
            "Fused %d results.",
            len(fused),
        )

        return state