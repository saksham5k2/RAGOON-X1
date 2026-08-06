class ParentDocumentRetriever:

    def __init__(
        self,
        document_store,
    ):
        self.document_store = document_store

    def retrieve(
        self,
        chunks,
    ):

        parents = {}

        for chunk in chunks:

            document_id = chunk.document_id

            if document_id not in parents:

                document = (
                    self.document_store.get(
                        document_id
                    )
                )

                if document is not None:

                    parents[
                        document_id
                    ] = document

        return list(
            parents.values()
        )