from qdrant_client import QdrantClient

client = QdrantClient(path="storage/qdrant_store")

print(client.get_collections())

print(client.get_collection("wikipedia"))

client.close()