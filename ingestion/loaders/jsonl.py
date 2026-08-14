import json
from pathlib import Path

from models.document import Document
from ingestion.loaders.base import BaseDocumentLoader


class JSONLDocumentLoader(BaseDocumentLoader):

    def __init__(
        self,
        path,
        text_field="text",
        title_field=None,
        metadata_fields=None,
    ):
        self.path = Path(path)
        self.text_field = text_field
        self.title_field = title_field
        self.metadata_fields = metadata_fields or []

    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as f:

            for index, line in enumerate(f):

                if not line.strip():
                    continue

                record = json.loads(line)

                text = str(
                    record.get(
                        self.text_field,
                        "",
                    )
                ).strip()

                if not text:
                    continue

                title = self._get_title(
                    record,
                    index,
                )

                metadata = {
                    field: record.get(field)
                    for field in self.metadata_fields
                    if field in record
                }

                yield Document(
                    id=str(index),
                    title=title,
                    text=text,
                    metadata=metadata,
                )

    def _get_title(
        self,
        record,
        index,
    ):

        if self.title_field:

            title = record.get(
                self.title_field
            )

            if title:
                return str(title)

        return f"Document {index + 1}"