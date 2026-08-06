from embeddings.factory import EmbeddingFactory
from app.settings import EMBEDDING_MODEL

model = EmbeddingFactory.create(EMBEDDING_MODEL)

texts = [
    "Albert Einstein was a physicist.",
    "The Eiffel Tower is in Paris.",
]

vectors = model.embed(texts)

print(f"Vectors: {len(vectors)}")
print(f"Dimensions: {len(vectors[0])}")