import hashlib

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from storage.base import BaseVectorStore

from app.settings import (
    QDRANT_PATH,
    COLLECTION_NAME,
    EMBEDDING_DIM,
)


class QdrantStore(BaseVectorStore):

    def __init__(self):
        self.client = QdrantClient(path=QDRANT_PATH)

    def create_collection(self):

        collections = self.client.get_collections().collections

        names = [collection.name for collection in collections]

        if COLLECTION_NAME not in names:

            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=EMBEDDING_DIM,
                    distance=Distance.COSINE,
                ),
            )

            print(f"Created collection: {COLLECTION_NAME}")

        else:
            print(f"Collection already exists: {COLLECTION_NAME}")

    def _generate_point_id(self, chunk_id: str) -> int:

        digest = hashlib.sha256(
            chunk_id.encode("utf-8")
        ).digest()

        return int.from_bytes(
            digest[:8],
            byteorder="big",
            signed=False,
        )

    def add(self, chunks):

        if not chunks:
            return

        points = []

        for chunk in chunks:

            if chunk.embedding is None:
                continue

            points.append(
                PointStruct(
                    id=self._generate_point_id(chunk.chunk_id),
                    vector=chunk.embedding,
                    payload={
                        "chunk_id": chunk.chunk_id,
                        "document_id": chunk.document_id,
                        "text": chunk.text,
                        "metadata": chunk.metadata,
                    },
                )
            )

        if points:

            self.client.upsert(
                collection_name=COLLECTION_NAME,
                points=points,
                wait=True,
            )

    def search(self, embedding, limit=10):

        response = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=embedding,
            limit=limit,
        )

        return response.points

    def close(self):
        self.client.close()