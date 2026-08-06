from collections import defaultdict


class ReciprocalRankFusion:

    def __init__(self, k=60):
        self.k = k

    def fuse(self, ranked_lists):

        scores = defaultdict(float)
        documents = {}

        for results in ranked_lists:

            for rank, result in enumerate(results, start=1):

                chunk = result.payload["chunk_id"]

                scores[chunk] += (
                    1.0 /
                    (self.k + rank)
                )

                documents[chunk] = result

        reranked = sorted(
            documents.values(),
            key=lambda x: scores[
                x.payload["chunk_id"]
            ],
            reverse=True,
        )

        return reranked