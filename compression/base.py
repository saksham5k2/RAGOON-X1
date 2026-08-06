from abc import ABC, abstractmethod

from chunking.chunk import Chunk


class BaseCompressor(ABC):

    @abstractmethod
    def compress(
        self,
        query: str,
        chunks: list[Chunk],
    ) -> list[Chunk]:
        """
        Compress retrieved chunks while preserving
        information useful for answering the query.
        """
        pass