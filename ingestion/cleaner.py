import re
import mwparserfromhell

class DocumentCleaner:
    def clean(self, text: str) -> str:
        code = mwparserfromhell.parse(text)
        text = code.strip_code()
        text = re.sub(r"==+\s*(.*?)\s*==+", r"\1", text)
        text = re.sub(r"\[\[Category:.*?\]\]", "", text)
        text = re.sub(r"\[\[File:.*?\]\]", "", text)
        text = re.sub(r"\[\[Image:.*?\]\]", "", text)
        text = re.sub(r"<ref.*?>.*?</ref>", "", text, flags=re.DOTALL)
        text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.DOTALL)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()