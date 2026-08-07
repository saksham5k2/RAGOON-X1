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

        chunks = self.retrieval.retrieve(
            query
        )

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