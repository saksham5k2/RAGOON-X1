from rag.pipeline import RagPipeline


def main():

    rag = RagPipeline()

    try:

        while True:

            query = input(
                "\nQuestion (type 'exit' to quit): "
            )

            if query.lower() == "exit":
                break

            response = rag.answer(query)

            print("\n")
            print("=" * 80)
            print("ANSWER")
            print("=" * 80)
            print(response.answer)

            print("\n")
            print("=" * 80)
            print("SOURCES")
            print("=" * 80)

            for i, chunk in enumerate(
                response.sources,
                start=1,
            ):

                print(f"\n[{i}]")
                print("Document:", chunk.document_id)
                print("Chunk:", chunk.chunk_id)
                print()
                print(chunk.text[:300])

    finally:

        rag.close()


if __name__ == "__main__":
    main()