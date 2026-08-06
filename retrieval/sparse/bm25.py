import math

from retrieval.sparse.index import InvertedIndex
from retrieval.sparse.tokenizer import Tokenizer


class BM25:

    def __init__(
        self,
        index: InvertedIndex,
        k1: float = 1.5,
        b: float = 0.75,
    ):

        self.index = index
        self.tokenizer = Tokenizer()

        self.k1 = k1
        self.b = b

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
    ):

        scores = {}

        tokens = self.tokenizer.tokenize(query)

        avgdl = self.index.average_document_length()

        N = self.index.total_documents

        for token in tokens:

            postings = self.index.lookup(token)

            if not postings:
                continue

            df = self.index.document_frequency(token)

            idf = math.log(
                (N - df + 0.5) /
                (df + 0.5)
                + 1
            )

            for chunk_id, tf in postings.items():

                dl = self.index.document_lengths[
                    chunk_id
                ]

                numerator = tf * (
                    self.k1 + 1
                )

                denominator = (
                    tf
                    + self.k1
                    * (
                        1
                        - self.b
                        + self.b
                        * dl
                        / avgdl
                    )
                )

                score = idf * (
                    numerator /
                    denominator
                )

                scores[chunk_id] = (
                    scores.get(chunk_id, 0)
                    + score
                )

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            (
                self.index.documents[
                    chunk_id
                ],
                score,
            )
            for chunk_id, score
            in ranked[:top_k]
        ]