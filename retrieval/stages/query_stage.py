from ragoonx.logging import logger

from retrieval.stages.base import RetrievalStage


class QueryStage(RetrievalStage):

    def __init__(
        self,
        query_rewriter,
        multi_query_generator,
    ):
        self.query_rewriter = query_rewriter
        self.multi_query_generator = (
            multi_query_generator
        )

    def run(
        self,
        state,
    ):

        query = state["query"]

        rewritten = self.query_rewriter.rewrite(
            query
        )

        queries = (
            self.multi_query_generator.generate(
                rewritten
            )
        )

        logger.info(
            "Original Query : %s",
            query,
        )

        logger.info(
            "Rewritten Query: %s",
            rewritten,
        )

        logger.info(
            "Generated Queries:"
        )

        for q in queries:

            logger.info(
                "  • %s",
                q,
            )

        state["rewritten_query"] = rewritten
        state["queries"] = queries

        return state