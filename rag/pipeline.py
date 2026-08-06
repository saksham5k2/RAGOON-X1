from retrieval.pipeline import RetrievalPipeline
from generation.pipeline import GenerationPipeline

from rag.response import RagResponse


class RagPipeline:

    def __init__(self):

        self.retrieval = RetrievalPipeline()

        self.generation = GenerationPipeline()

    def answer(
        self,
        query: str,
    ):

        retrieved = self.retrieval.retrieve(
            query
        )

        chunks = [
            chunk
            for chunk, _ in retrieved
        ]

        response = self.generation.generate(
            query,
            chunks,
        )

        return RagResponse(
            query=query,
            answer=response.answer,
            prompt=response.prompt,
            sources=chunks,
        )

    def close(self):

        self.retrieval.close()