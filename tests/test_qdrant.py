from qdrant_client import QdrantClient

client = QdrantClient(path="storage/qdrant_store")

print("Connected!")

print(client.get_collections())

client.close()

print("Closed!")