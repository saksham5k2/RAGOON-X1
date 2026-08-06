from retrieval.pipeline import RetrievalPipeline


def main():

    pipeline = RetrievalPipeline()

    try:

        while True:

            query = input("\nQuery (type 'exit' to quit): ").strip()

            if query.lower() == "exit":
                break

            results = pipeline.retrieve(query)

            print()

            if not results:
                print("No results found.")
                continue

            for rank, (chunk, score) in enumerate(results, start=1):

                print("=" * 80)
                print(f"Rank #{rank}")
                print(f"Fusion Score : {score:.6f}")
                print(f"Chunk ID     : {chunk.chunk_id}")
                print(f"Document ID  : {chunk.document_id}")
                print()
                print(chunk.text[:400])
                print()

    finally:
        pipeline.close()


if __name__ == "__main__":
    main()