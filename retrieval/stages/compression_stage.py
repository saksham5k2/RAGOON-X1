from ragoonx.logging import logger
import app.settings as settings

from retrieval.stages.base import RetrievalStage


class CompressionStage(RetrievalStage):

    def __init__(self, compressor):
        self.compressor = compressor

    def run(self, state):

        compressed = self.compressor.compress(
            state["query"],
            state["reranked"],
        )

        state["compressed"] = compressed

        logger.info(
            "Compressed %d chunks.",
            len(compressed),
        )

        if settings.DEBUG:

            print("\n" + "=" * 70)
            print("DEBUG — COMPRESSED CONTEXT")
            print("=" * 70)

            for i, chunk in enumerate(
                compressed,
                1,
            ):

                print(
                    f"\n--- Chunk {i} ---"
                )

                print(
                    chunk.text[:1000]
                )

            print("=" * 70 + "\n")

        return state