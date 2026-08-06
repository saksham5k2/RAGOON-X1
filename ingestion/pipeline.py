from ingestion.wikipedia_parser import WikipediaParser
from ingestion.cleaner import DocumentCleaner
from ingestion.metadata import MetadataExtractor

from chunking.factory import ChunkerFactory
from embeddings.factory import EmbeddingFactory

from models.ingestion_result import IngestionResult

from storage.factory import StorageFactory

from app.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    CHUNK_STRATEGY,
    EMBEDDING_MODEL,
    MAX_PAGES,
)


class IngestionPipeline:

    def __init__(self, xml_path):

        self.parser = WikipediaParser(xml_path)

        self.cleaner = DocumentCleaner()

        self.metadata = MetadataExtractor()

        self.chunker = ChunkerFactory.create(
            CHUNK_STRATEGY,
            CHUNK_SIZE,
            CHUNK_OVERLAP,
        )

        self.embedding_model = (
            EmbeddingFactory.create(
                EMBEDDING_MODEL
            )
        )

        self.document_store = (
            StorageFactory.create_document_store()
        )

    def run(self):
        """
        Pipeline

        Wikipedia XML
              ↓
        Parser
              ↓
        Cleaner
              ↓
        Metadata
              ↓
        Document Store
              ↓
        Chunker
              ↓
        Embedding
              ↓
        Yield
        """

        for i, document in enumerate(
            self.parser.parse()
        ):

            if (
                MAX_PAGES is not None
                and i >= MAX_PAGES
            ):
                break

            # -------------------------
            # Clean
            # -------------------------

            document.text = self.cleaner.clean(
                document.text
            )

            # -------------------------
            # Metadata
            # -------------------------

            document = self.metadata.extract(
                document
            )

            # -------------------------
            # Save Full Document
            # -------------------------

            self.document_store.add(
                document
            )

            # -------------------------
            # Chunk
            # -------------------------

            chunks = self.chunker.chunk(
                document
            )

            # -------------------------
            # Embeddings
            # -------------------------

            texts = [
                chunk.text
                for chunk in chunks
            ]

            embeddings = (
                self.embedding_model.embed(
                    texts
                )
            )

            for chunk, embedding in zip(
                chunks,
                embeddings,
            ):
                chunk.embedding = embedding

            yield IngestionResult(
                document=document,
                chunks=chunks,
            )

    def close(self):

        self.document_store.close()