import json
import os

from models.document import Document

from storage.document_store import (
    BaseDocumentStore,
)


class JsonDocumentStore(
    BaseDocumentStore
):

    def __init__(self, path):

        self.path = path

        if os.path.exists(path):

            with open(
                path,
                "r",
                encoding="utf-8",
            ) as f:

                self.documents = json.load(f)

        else:

            self.documents = {}

    def add(
        self,
        document,
    ):

        self.documents[
            str(document.id)
        ] = {

            "id": document.id,

            "title": document.title,

            "text": document.text,

            "metadata": document.metadata,

        }

    def get(
        self,
        document_id,
    ):

        data = self.documents.get(
            str(document_id)
        )

        if data is None:
            return None

        return Document(

            id=data["id"],

            title=data["title"],

            text=data["text"],

            metadata=data["metadata"],

        )

    def close(self):

        with open(
            self.path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(

                self.documents,

                f,

                ensure_ascii=False,

                indent=2,

            )