from app.settings import (
    RERANKER_MODEL,
)

from reranking.cross_encoder import (
    CrossEncoderReranker,
)


class RerankerFactory:

    @staticmethod
    def create():

        return CrossEncoderReranker(
            RERANKER_MODEL
        )