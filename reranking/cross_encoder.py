from sentence_transformers import CrossEncoder

from reranking.base import BaseReranker


class CrossEncoderReranker(BaseReranker):

    def __init__(
        self,
        model_name: str,
    ):

        self.model = CrossEncoder(
            model_name
        )

    def rerank(
        self,
        query: str,
        results,
        top_k: int,
    ):

        if not results:
            return []

        sentence_pairs = [

            (
                query,
                chunk.text,
            )

            for chunk, _ in results

        ]

        scores = self.model.predict(
            sentence_pairs
        )

        reranked = []

        for (chunk, _), score in zip(
            results,
            scores,
        ):

            reranked.append(
                (
                    chunk,
                    float(score),
                )
            )

        reranked.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        # Return only Chunk objects
        return [

            chunk

            for chunk, _
            in reranked[:top_k]

        ]