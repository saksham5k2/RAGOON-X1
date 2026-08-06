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

        print("\nGenerated Queries:")

        for query in queries:
            print(f" • {query}")

        state["queries"] = queries

        return state