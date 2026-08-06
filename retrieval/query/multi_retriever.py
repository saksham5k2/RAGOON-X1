class MultiQueryRetriever:

    def __init__(self, retriever):

        self.retriever = retriever

    def retrieve(
        self,
        queries,
        top_k=10,
    ):

        merged = {}

        for query in queries:

            results = self.retriever.retrieve(
                query=query,
                top_k=top_k,
            )

            for chunk, score in results:

                if (
                    chunk.chunk_id not in merged
                    or score > merged[chunk.chunk_id][1]
                ):
                    merged[chunk.chunk_id] = (
                        chunk,
                        score,
                    )

        results = sorted(
            merged.values(),
            key=lambda item: item[1],
            reverse=True,
        )

        return results[:top_k]