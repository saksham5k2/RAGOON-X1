from copy import deepcopy

from chunking.chunk import Chunk

from compression.base import BaseCompressor
from compression.sentence_splitter import SentenceSplitter


class EmbeddingCompressor(BaseCompressor):

    def __init__(
        self,
        embedding_model,
        keep_sentences=3,
    ):

        self.embedding_model = embedding_model
        self.keep_sentences = keep_sentences
        self.splitter = SentenceSplitter()

    def compress(
        self,
        query: str,
        chunks: list[Chunk],
    ) -> list[Chunk]:

        compressed = []

        query_embedding = (
            self.embedding_model.embed_query(query)
        )

        for chunk in chunks:

            sentences = self.splitter.split(
                chunk.text
            )

            if len(sentences) <= self.keep_sentences:

                compressed.append(chunk)
                continue

            sentence_embeddings = (
                self.embedding_model.embed_documents(
                    sentences
                )
            )

            scores = []

            for sentence, embedding in zip(
                sentences,
                sentence_embeddings,
            ):

                similarity = sum(
                    q * s
                    for q, s in zip(
                        query_embedding,
                        embedding,
                    )
                )

                scores.append(
                    (
                        sentence,
                        similarity,
                    )
                )

            scores.sort(
                key=lambda x: x[1],
                reverse=True,
            )

            selected = [
                sentence
                for sentence, _
                in scores[:self.keep_sentences]
            ]

            new_chunk = deepcopy(chunk)

            new_chunk.text = " ".join(selected)

            compressed.append(new_chunk)

        return compressed