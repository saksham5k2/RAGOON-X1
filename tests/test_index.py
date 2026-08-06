from retrieval.sparse.index import InvertedIndex

from ingestion.pipeline import IngestionPipeline

from app.settings import WIKIPEDIA_DUMP


pipeline = IngestionPipeline(WIKIPEDIA_DUMP)

index = InvertedIndex()

for result in pipeline.run():

    index.add(result.chunks)

print(index.lookup("computer"))

print(index.lookup("accessibility"))

print(index.lookup("afghanistan"))