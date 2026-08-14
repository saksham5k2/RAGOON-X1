from ingestion.loaders import JSONLDocumentLoader

from ingestion.pipeline import (
    IngestionPipeline,
)

from storage.factory import (
    StorageFactory,
)


DATASET_PATH = (
    "data/raw/stencore/"
    "stencore_10k.jsonl"
)


def main():

    loader = JSONLDocumentLoader(
        DATASET_PATH,
        text_field="text",
        metadata_fields=[
            "source",
            "source_url",
            "license",
        ],
    )

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


if __name__ == "__main__":
    main()