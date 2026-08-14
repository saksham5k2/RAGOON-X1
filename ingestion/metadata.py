class MetadataExtractor:

    def extract(self, document):

        metadata = document.metadata

        metadata["word_count"] = (
            len(document.text.split())
        )

        metadata["char_count"] = (
            len(document.text)
        )

        metadata["title"] = (
            document.title
        )

        metadata["language"] = "en"

        metadata["estimated_read_time"] = max(
            1,
            metadata["word_count"] // 200
        )

        document.metadata = metadata

        return document