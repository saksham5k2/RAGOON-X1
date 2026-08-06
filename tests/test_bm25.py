from ingestion.pipeline import IngestionPipeline

from retrieval.sparse.index import InvertedIndex
from retrieval.sparse.bm25 import BM25

from app.settings import WIKIPEDIA_DUMP


pipeline = IngestionPipeline(
    WIKIPEDIA_DUMP
)

index = InvertedIndex()

for result in pipeline.run():

    index.add(result.chunks)

bm25 = BM25(index)

results = bm25.retrieve(
    "computer accessibility"
)

for i, (chunk, score) in enumerate(results, start=1):

    print("=" * 80)
    print(f"Rank {i}")
    print(score)
    print(chunk.chunk_id)
    print(chunk.text[:300])