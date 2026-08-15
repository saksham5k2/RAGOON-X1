from retrieval.pipeline import RetrievalPipeline
from generation.pipeline import GenerationPipeline

from rag.response import RagResponse

from ragoonx.config import ConfigLoader


class RagPipeline:

    def __init__(self):

        config = ConfigLoader.load()

        self.retrieval = RetrievalPipeline()

        self.generation = GenerationPipeline(
            config.llm
        )

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
