from lxml import etree
from ingestion.parser import BaseParser
from ingestion.document import Document

class WikipediaParser(BaseParser):

    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse(self):
        context = etree.iterparse(
            self.xml_path,
            events=("end",),
            tag="{*}page"
        )

        for event, page in context:
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
                source="Wikipedia"
            )

            yield document
            page.clear()