from retrieval.stages.base import RetrievalStage


class QueryRewriteStage(RetrievalStage):

    def __init__(
        self,
        query_rewriter,
    ):
        self.query_rewriter = query_rewriter

    def run(
        self,
        state,
    ):

        rewritten_query = (
            self.query_rewriter.rewrite(
                state["query"]
            )
        )

        print(f"\nOriginal Query : {state['query']}")
        print(f"Rewritten Query: {rewritten_query}")

        state["rewritten_query"] = rewritten_query

        return state