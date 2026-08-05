from ingestion.wikipedia_parser import WikipediaParser
from ingestion.cleaner import DocumentCleaner
from ingestion.metadata import MetadataExtractor

from chunking.factory import ChunkerFactory
from app.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    CHUNK_STRATEGY,
)

class IngestionPipeline:
    def __init__(self, xml_path):
        self.parser = WikipediaParser(xml_path)
        self.cleaner = DocumentCleaner()
        self.metadata = MetadataExtractor()
        self.chunker = ChunkerFactory.create(
            CHUNK_STRATEGY,
            CHUNK_SIZE,
            CHUNK_OVERLAP
        )

    def run(self):
        for document in self.parser.parse():

            print("RAW:")
            print(document.text)
            print("=" * 60)
            document.text = self.cleaner.clean(document.text)
            print("CLEANED:")
            document = self.metadata.extract(document)
            chunks = self.chunker.chunk(document)

            for chunk in chunks:
                print(chunk.chunk_id)
                print(chunk.text)
                print("-" * 40)