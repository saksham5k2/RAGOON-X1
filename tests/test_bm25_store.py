from storage.bm25_store import BM25Store

from app.settings import BM25_INDEX_PATH


store = BM25Store()

store.load(
    BM25_INDEX_PATH
)

results = store.search(
    "computer accessibility"
)

for i, (chunk, score) in enumerate(results, start=1):

    print("=" * 80)
    print(f"Rank {i}")
    print(f"Score: {score:.4f}")
    print(chunk.chunk_id)
    print(chunk.text[:300])