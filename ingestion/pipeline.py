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
    INDEX_BATCH_SIZE,
)


class IngestionPipeline:

    def __init__(self, loader):

        self.loader = loader

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
        Generic ingestion pipeline

        Documents
              ↓
        Cleaner
              ↓
        Metadata
              ↓
        Document Store
              ↓
        Chunker
              ↓
        Batch Embedding
              ↓
        Yield Results
        """

        batch = []

        processed = 0

        for document in self.loader.load():

            if (
                MAX_PAGES is not None
                and processed >= MAX_PAGES
            ):
                break

            # ---------------------------------
            # Clean
            # ---------------------------------

            document.text = (
                self.cleaner.clean(
                    document.text
                )
            )

            # ---------------------------------
            # Metadata
            # ---------------------------------

            document = (
                self.metadata.extract(
                    document
                )
            )

            # ---------------------------------
            # Save Full Document
            # ---------------------------------

            self.document_store.add(
                document
            )

            # ---------------------------------
            # Chunk
            # ---------------------------------

            chunks = self.chunker.chunk(
                document
            )

            batch.append(
                (
                    document,
                    chunks,
                )
            )

            processed += 1

            # ---------------------------------
            # Process Batch
            # ---------------------------------

            if len(batch) >= INDEX_BATCH_SIZE:

                yield from self._process_batch(
                    batch
                )

                batch = []

        # ---------------------------------
        # Process Remaining Documents
        # ---------------------------------

        if batch:

            yield from self._process_batch(
                batch
            )

    def _process_batch(
        self,
        batch,
    ):

        # ---------------------------------
        # Collect Chunks
        # ---------------------------------

        all_chunks = []

        for document, chunks in batch:

            all_chunks.extend(
                chunks
            )

        if not all_chunks:

            return

        # ---------------------------------
        # Batch Embedding
        # ---------------------------------

        texts = [
            chunk.text
            for chunk in all_chunks
        ]

        embeddings = (
            self.embedding_model.embed_documents(
                texts
            )
        )

        # ---------------------------------
        # Attach Embeddings
        # ---------------------------------

        for chunk, embedding in zip(
            all_chunks,
            embeddings,
        ):

            chunk.embedding = embedding

        # ---------------------------------
        # Return Document Results
        # ---------------------------------

        offset = 0

        for document, chunks in batch:

            count = len(chunks)

            document_chunks = (
                all_chunks[
                    offset:
                    offset + count
                ]
            )

            offset += count

            yield IngestionResult(
                document=document,
                chunks=document_chunks,
            )

    def close(self):

        self.document_store.close()
