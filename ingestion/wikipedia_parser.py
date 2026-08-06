import bz2
from pathlib import Path

from lxml import etree
from ingestion.parser import BaseParser
from ingestion.document import Document

class WikipediaParser(BaseParser):

    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse(self):
        path = Path(self.xml_path)
        opener = bz2.open if path.suffix == ".bz2" else open

        with opener(path, "rb") as xml_file:
            context = etree.iterparse(
                xml_file,
                events=("end",),
                tag="{*}page",
            )

            for _, page in context:
                title = page.findtext("{*}title")
                page_id = page.findtext("{*}id")
                revision = page.find("{*}revision")
                text = ""

                if revision is not None:
                    text = revision.findtext("{*}text") or ""

                document = Document(
                    id=page_id,
                    title=title,
                    text=text,
                    source="Wikipedia",
                )

                yield document
                page.clear()
