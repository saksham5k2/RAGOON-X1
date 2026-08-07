from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class MultiQueryStage(RetrievalStage):

    def __init__(
        self,
        generator,
    ):
        self.generator = generator

    def run(
        self,
        state,
    ):

        base_query = state.get(
            "hyde_document",
            state["rewritten_query"],
        )

        queries = self.generator.generate(
            base_query
        )

        logger.info(
            "Generated Queries:"
        )

        for query in queries:

            logger.info(
                " • %s",
                query,
            )

        state["queries"] = queries

        return state