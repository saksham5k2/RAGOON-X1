# from app.settings import *
# print(f"APP_NAME: {APP_NAME}")
# print(f"APP_VERSION: {APP_VERSION}")
# print(f"ENVIRONMENT: {ENVIRONMENT}")
# print(f"LLM_PROVIDER: {LLM_PROVIDER}")
# print(f"LLM_MODEL: {LLM_MODEL}")
# print(f"VECTOR_DB_PROVIDER: {VECTOR_DB_PROVIDER}")
# print(f"EMBEDDING_MODEL: {EMBEDDING_MODEL}")
# print(f"TOP_K: {TOP_K}")
# print(f"CHUNK_SIZE: {CHUNK_SIZE}")
# print(f"CHUNK_OVERLAP: {CHUNK_OVERLAP}")

from ingestion.pipeline import IngestionPipeline
pipeline = IngestionPipeline("data/sample.xml")
pipeline.run()