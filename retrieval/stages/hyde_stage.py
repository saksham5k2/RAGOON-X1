from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class HyDEStage(RetrievalStage):

    def __init__(
        self,
        hyde_generator,
    ):
        self.hyde_generator = hyde_generator

    def run(
        self,
        state,
    ):

        hypothetical_document = (
            self.hyde_generator.generate(
                state["rewritten_query"]
            )
        )

        logger.info(
            "HyDE Document:"
        )

        logger.info(
            "%s",
            "-" * 80,
        )

        logger.info(
            "%s",
            hypothetical_document,
        )

        logger.info(
            "%s",
            "-" * 80,
        )

        state["hyde_document"] = hypothetical_document

        return state