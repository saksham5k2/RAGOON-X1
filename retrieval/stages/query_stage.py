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
        query: str,
    ):

        rewritten = self.query_rewriter.rewrite(
            query
        )

        queries = (
            self.multi_query_generator.generate(
                rewritten
            )
        )

        return {
            "original_query": query,
            "rewritten_query": rewritten,
            "queries": queries,
        }