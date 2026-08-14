from rag.pipeline import RagPipeline

from ragoonx.config import ConfigLoader
from ragoonx.config.sync import (
    ConfigSynchronizer,
)

from ingestion.pipeline import (
    IngestionPipeline,
)

from ingestion.loaders import (
    JSONLDocumentLoader,
)

from storage.factory import (
    StorageFactory,
)

import app.settings as settings


config = ConfigLoader.load()
ConfigSynchronizer.synchronize(config)


class Ragoon:

    def __init__(self):

        # Lazy initialization
        self.pipeline = None

    def _get_pipeline(self):

        if self.pipeline is None:

            self.pipeline = RagPipeline()

        return self.pipeline

    def query(
        self,
        query: str,
    ):

        return self._get_pipeline().answer(
            query
        )

    def ingest(
        self,
        path=None,
    ):

        # ---------------------------------
        # Determine ingestion source
        # ---------------------------------

        source_path = (
            path
            if path
            else settings.WIKIPEDIA_DUMP
        )

        if not source_path:

            raise ValueError(
                "No ingestion source provided."
            )

        # ---------------------------------
        # Create document loader
        # ---------------------------------

        loader = JSONLDocumentLoader(
            source_path,
            text_field="text",
            metadata_fields=[
                "source",
                "source_url",
                "license",
            ],
        )

        # ---------------------------------
        # Create ingestion pipeline
        # ---------------------------------

        pipeline = IngestionPipeline(
            loader
        )

        vector_store = (
            StorageFactory.create_vector_store()
        )

        sparse_store = (
            StorageFactory.create_sparse_store()
        )

        try:

            vector_store.create_collection()

            total_chunks = 0

            all_chunks = []

            for result in pipeline.run():

                vector_store.add(
                    result.chunks
                )

                all_chunks.extend(
                    result.chunks
                )

                total_chunks += len(
                    result.chunks
                )

                print(
                    f"Indexed: {result.document.title} "
                    f"({len(result.chunks)} chunks)"
                )

            sparse_store.build(
                all_chunks
            )

            print(
                f"\nTotal chunks indexed: {total_chunks}"
            )

        finally:

            pipeline.close()
            vector_store.close()
            sparse_store.close()

    def chat(self):

        print("\nRAGOON-X1 Chat")
        print("Type 'exit' to quit.\n")

        while True:

            query = input("> ")

            if query.lower() in [
                "exit",
                "quit",
            ]:
                break

            response = self.query(
                query
            )

            print(
                f"\n{response.answer}\n"
            )

    def close(self):

        if self.pipeline is not None:

            self.pipeline.close()