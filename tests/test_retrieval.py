from embeddings.factory import EmbeddingFactory
from storage.factory import StorageFactory
from retrieval.factory import RetrieverFactory

from app.settings import EMBEDDING_MODEL


embedding_model = EmbeddingFactory.create(
    EMBEDDING_MODEL
)

vector_store = StorageFactory.create()

retriever = RetrieverFactory.create_dense(
    embedding_model,
    vector_store,
)

results = retriever.retrieve(
    "computer accessibility",
    top_k=5,
)

for i, result in enumerate(results, start=1):

    print("=" * 80)

    print(f"Result {i}")
    print("Score:", result.score)

    payload = result.payload

    print("Chunk ID:", payload["chunk_id"])
    print("Document:", payload["document_id"])

    print()
    print(payload["text"][:300])

vector_store.close()