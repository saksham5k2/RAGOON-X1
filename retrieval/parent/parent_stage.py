from retrieval.stages.base import RetrievalStage


class ParentStage(RetrievalStage):

    def __init__(
        self,
        parent_retriever,
    ):
        self.parent_retriever = (
            parent_retriever
        )

    def run(
        self,
        state,
    ):

        chunks = state["retrieved"]

        documents = (
            self.parent_retriever.retrieve(
                chunks
            )
        )

        state["parent_documents"] = (
            documents
        )

        print(
            f"\nExpanded to "
            f"{len(documents)} parent documents."
        )

        return state