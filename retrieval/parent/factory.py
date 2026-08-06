from retrieval.parent.retriever import (
    ParentDocumentRetriever,
)


class ParentRetrieverFactory:

    @staticmethod
    def create(
        document_store,
    ):

        return ParentDocumentRetriever(
            document_store
        )