from app.settings import EMBEDDING_MODEL

from embeddings.factory import EmbeddingFactory

from compression.embedding_compressor import (
    EmbeddingCompressor,
)


class CompressorFactory:

    @staticmethod
    def create():

        embedding_model = (
            EmbeddingFactory.create(
                EMBEDDING_MODEL
            )
        )

        return EmbeddingCompressor(
            embedding_model
        )