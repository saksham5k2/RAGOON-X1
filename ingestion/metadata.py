import re
class MetadataExtractor:

    def extract(self, document):
        metadata = {}
        metadata["word_count"] = len(document.text.split())
        metadata["char_count"] = len(document.text)
        metadata["source"] = document.source
        metadata["title"] = document.title
        metadata["language"] = "en"
        metadata["estimated_read_time"] = max(
            1,
            metadata["word_count"] // 200
        )

        document.metadata.update(metadata)
        return document