from chunking.base_chunker import BaseChunker
from chunking.chunk import Chunk

class CharacterChunker(BaseChunker):

    def __init__(self, chunk_size, overlap):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document):
        chunks = []
        text = document.text
        start = 0
        chunk_number = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk_text = text[start:end]
            chunks.append(
                Chunk(
                    chunk_id=f"{document.id}_{chunk_number}",
                    document_id=document.id,
                    text=chunk_text,
                    metadata=document.metadata.copy()
                )
            )
            start += self.chunk_size - self.overlap
            chunk_number += 1
        return chunks