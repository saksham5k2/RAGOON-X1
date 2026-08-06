from ingestion.pipeline import IngestionPipeline
from retrieval.sparse.index import InvertedIndex

from app.settings import WIKIPEDIA_DUMP


pipeline = IngestionPipeline(
    WIKIPEDIA_DUMP
)

index = InvertedIndex()

for result in pipeline.run():

    index.add(result.chunks)

print()

print("Total Docs:")
print(index.total_documents)

print()

print("Average Length:")
print(index.average_document_length())

print()

print("Document Frequency of 'computer':")
print(index.document_frequency("computer"))

print()

print("Posting List:")
print(index.lookup("computer"))