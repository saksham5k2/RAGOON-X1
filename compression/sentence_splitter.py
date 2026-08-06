import re


class SentenceSplitter:

    def split(
        self,
        text: str,
    ) -> list[str]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text,
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]