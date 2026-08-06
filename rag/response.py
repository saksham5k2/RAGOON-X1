from dataclasses import dataclass


@dataclass
class RagResponse:

    query: str

    answer: str

    sources: list

    prompt: str