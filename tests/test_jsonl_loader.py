from ingestion.loaders import JSONLDocumentLoader


PATH = (
    "data/raw/stencore/"
    "stencore_10k.jsonl"
)


def main():

    loader = JSONLDocumentLoader(
        PATH,
        text_field="text",
        metadata_fields=[
            "source",
            "source_url",
            "license",
        ],
    )

    documents = loader.load()

    count = 0

    for document in documents:

        count += 1

        if count <= 3:

            print("\n" + "=" * 60)

            print(f"ID: {document.id}")
            print(f"Title: {document.title}")
            print(f"Text length: {len(document.text)}")
            print(f"Metadata: {document.metadata}")

    print(
        f"\nDocuments loaded: {count}"
    )

    print(
        f"Documents loaded: {len(documents)}"
    )

    for document in documents[:3]:

        print("\n" + "=" * 60)

        print(
            f"ID: {document.id}"
        )

        print(
            f"Title: {document.title}"
        )

        print(
            f"Text length: {len(document.text)}"
        )

        print(
            f"Metadata: {document.metadata}"
        )


if __name__ == "__main__":
    main()