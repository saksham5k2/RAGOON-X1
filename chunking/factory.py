from chunking.character_chunker import CharacterChunker
from chunking.recursive_chunker import RecursiveChunker

class ChunkerFactory:
    @staticmethod
    def create(
        strategy,
        chunk_size,
        overlap
    ):

        if strategy == "character":
            return CharacterChunker(
                chunk_size,
                overlap
            )

        elif strategy == "recursive":
            return RecursiveChunker(
                chunk_size,
                overlap
            )

        raise ValueError(
            "Unknown chunk strategy"
        )