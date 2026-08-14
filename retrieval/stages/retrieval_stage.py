from retrieval.stages.base import RetrievalStage


class RetrievalStageImpl(RetrievalStage):

    def __init__(
        self,
        retriever,
    ):
        self.retriever = retriever

    def run(
        self,
        state,
    ):

        retrieval_queries = state.get(
            "generated_queries",
            [state["rewritten_query"]],
        )

        retrieved = self.retriever.retrieve(
            retrieval_queries,
            top_k=state["top_k"] * 3,
        )

        state["retrieved"] = retrieved

        return state