from collections import defaultdict

from chunking.chunk import Chunk


class ReciprocalRankFusion:

    def __init__(self, k: int = 60):
        self.k = k

    def fuse(self, dense_results, sparse_results):

        fused_scores = defaultdict(float)
        chunks = {}

        # -----------------------------
        # Dense Results (Qdrant)
        # -----------------------------
        for rank, point in enumerate(dense_results, start=1):

            payload = point.payload

            chunk = Chunk(
                chunk_id=payload["chunk_id"],
                document_id=payload["document_id"],
                text=payload["text"],
                metadata=payload.get("metadata", {}),
            )

            chunks[chunk.chunk_id] = chunk

            fused_scores[chunk.chunk_id] += (
                1 / (self.k + rank)
            )

        # -----------------------------
        # Sparse Results (BM25)
        # -----------------------------
        for rank, (chunk, _) in enumerate(sparse_results, start=1):

            chunks[chunk.chunk_id] = chunk

            fused_scores[chunk.chunk_id] += (
                1 / (self.k + rank)
            )

        results = sorted(
            fused_scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            (chunks[chunk_id], score)
            for chunk_id, score in results
        ]