from dataclasses import dataclass

from ingestion.document import Document
from chunking.chunk import Chunk


@dataclass
class IngestionResult:
    document: Document
    chunks: list[Chunk]