import re

from chunking.base_chunker import BaseChunker
from chunking.chunk import Chunk

class RecursiveChunker(BaseChunker):
    def __init__(self, chunk_size, overlap):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.separators = [
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    def chunk(self, document):
        pieces = self._split(
            document.text,
            self.separators
        )

        chunks = []
        for i, piece in enumerate(pieces):
            chunks.append(
                Chunk(
                    chunk_id=f"{document.id}_{i}",
                    document_id=document.id,
                    text=piece,
                    metadata=document.metadata.copy()
                )
            )
        return chunks


    def _split(self, text, separators):
        if len(text) <= self.chunk_size:
            return [text]

        if not separators:
            return [
                text[i:i+self.chunk_size]
                for i in range(
                    0,
                    len(text),
                    self.chunk_size-self.overlap
                )

        ]   

        separator = separators[0]

        if separator == "":
            return [
                text[i:i+self.chunk_size]
                for i in range(
                    0,
                    len(text),
                    self.chunk_size-self.overlap
                )
            ]

        splits = text.split(separator)
        results = []
        current = ""
        for split in splits:
            candidate = current + separator + split if current else split
            if len(candidate) <= self.chunk_size:
                current = candidate
            else:
                if current:
                    results.extend(
                        self._split(
                            current,
                            separators[1:]
                        )
                    )
                current = split

        if current:
            results.extend(
                self._split(
                    current,
                    separators[1:]
                )
            )

        return results
    